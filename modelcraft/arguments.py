from typing import List, Optional
import argparse
import os
import gemmi
import numpy
import pandas
from . import __version__
from .contents import AsuContents
from .reflections import DataItem
from .structure import read_structure


_PARSER = argparse.ArgumentParser()
_PARSER.add_argument("-v", "--version", action="version", version=__version__)

_PARENT = argparse.ArgumentParser(add_help=False)
_GROUP = _PARENT.add_argument_group("required arguments (common)")
_GROUP.add_argument("--contents", required=True)
_GROUP = _PARENT.add_argument_group("optional arguments (common)")
_GROUP.add_argument("--model")
_GROUP.add_argument("--cycles", default=25, type=int)
_GROUP.add_argument("--auto-stop-cycles", default=4, type=int)
_GROUP.add_argument("--directory", default=".")
_GROUP.add_argument("--keep-jobs", action="store_true")
_GROUP.add_argument("--keep-logs", action="store_true")

_SUB_PARSERS = _PARSER.add_subparsers(dest="mode", required=True)

_XRAY = _SUB_PARSERS.add_parser("xray", parents=[_PARENT])
_GROUP = _XRAY.add_argument_group("required arguments (xray)")
_GROUP.add_argument("--data", required=True)
_GROUP = _XRAY.add_argument_group("optional arguments (xray)")
_GROUP.add_argument("--observations")
_GROUP.add_argument("--freerflag")
_GROUP.add_argument("--phases")
_GROUP.add_argument("--unbiased", action="store_true")
_GROUP.add_argument("--twinned", action="store_true")
_GROUP.add_argument("--basic", action="store_true")

_EM = _SUB_PARSERS.add_parser("em", parents=[_PARENT])
_GROUP = _EM.add_argument_group("required arguments (em)")
_GROUP.add_argument("--map", required=True)
_GROUP.add_argument("--resolution", type=float, required=True)


def parse(arguments: Optional[List[str]] = None) -> argparse.Namespace:
    args = _PARSER.parse_args(arguments)
    _basic_check(args)
    _check_paths(args)
    args.contents = AsuContents.from_file(args.contents)
    if args.mode == "xray":
        _parse_data_items(args)
    if args.mode == "em":
        _parse_map(args)
    if args.model:
        args.model = read_structure(args.model)
    return args


def _basic_check(args: argparse.Namespace):
    if args.cycles < 1:
        _PARSER.error("--cycles must be greater than 0")
    if args.mode == "em" and args.resolution <= 0:
        _PARSER.error("--resolution must be greater than 0")


def _check_paths(args: argparse.Namespace):
    for arg in ("contents", "data", "map", "model"):
        if hasattr(args, arg):
            path = getattr(args, arg)
            if path is not None:
                if not os.path.exists(path):
                    _PARSER.error("File not found: %s" % path)
                path = os.path.abspath(path)
                setattr(args, arg, path)


def _parse_data_items(args: argparse.Namespace):
    mtz = gemmi.read_mtz_file(args.data)
    args.observations = _parse_data_item(
        mtz, args.observations, ["FQ", "GLGL", "JQ", "KMKM"], "observations"
    )
    args.freer = _parse_data_item(mtz, args.freerflag, ["I"], "freerflag")
    if args.phases is not None or args.model is None:
        args.phases = _parse_data_item(mtz, args.phases, ["PW", "AAAA"], "phases")


def _parse_data_item(
    mtz: gemmi.Mtz, label: Optional[str], accepted_types: List[str], name: str
) -> DataItem:
    if label is None:
        options = []
        for types in accepted_types:
            items = DataItem.search(mtz, types, sequential=(types != "PW"))
            options.extend(items)
        if len(options) == 0:
            _PARSER.error(f"No suitable columns found for the {name}")
        if len(options) > 1:
            message = f"Multiple possible columns found for the {name}:"
            message += "\nPlease add one of the following options:"
            for option in options:
                message += f"\n--{name} {option.label()}"
            _PARSER.error(message)
        return options[0]
    item = DataItem(mtz, label)
    if item.types not in accepted_types:
        message = f"Column label '{label}' does not match type "
        message += " or ".join(accepted_types)
        _PARSER.error(message)
    return item


def _parse_map(args: argparse.Namespace):
    args.map = gemmi.read_ccp4_map(args.map)
    args.map.setup()
    array = numpy.array(args.map.grid, copy=False)
    if numpy.isnan(array).any():
        _PARSER.error("Map does not cover the full ASU")
    grid = gemmi.transform_map_to_f_phi(args.map.grid, half_l=True)
    data = grid.prepare_asu_data(dmin=args.resolution)
    mtz = gemmi.Mtz()
    mtz.cell = args.map.grid.unit_cell
    mtz.spacegroup = args.map.grid.spacegroup
    mtz.add_dataset("HKL_base")
    mtz.add_column("H", "H")
    mtz.add_column("K", "H")
    mtz.add_column("L", "H")
    mtz.add_column("F", "F")
    mtz.add_column("PHI", "P")
    mtz.set_data(data)
    mtz.update_reso()
    array = numpy.array(mtz, copy=True)
    data_frame = pandas.DataFrame(data=array, columns=mtz.column_labels())
    mtz.add_column("SIGF", "Q")
    data_frame["SIGF"] = 1.0
    mtz.add_column("FOM", "W")
    data_frame["FOM"] = 1.0
    mtz.set_data(data_frame.to_numpy())
    args.observations = DataItem(mtz, "F,SIGF")
    args.phases = DataItem(mtz, "PHI,FOM")
    args.fphi = DataItem(mtz, "F,PHI")
    args.freer = None

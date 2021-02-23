from modelcraft.contents import AsuContents


def _test_contents(pdbid: str, expected: list, selenomet: bool):
    contents = AsuContents(pdbid)
    assert contents.to_json() == expected
    assert contents.is_selenomet() == selenomet
    return contents


def test_1o6a():
    expected = {
        "copies": 2,
        "proteins": [
            {
                "sequence": "SETRKTEVPSDKLELLLDIPLKVTVELGRTRMTLKRVLEMIHGSIIELDKLTGEPVDILVNGKLIARGEVVVIDENFGVRITEIVSPKERLELLNE",
                "start": 1,
                "copies": 1,
                "modifications": ["M->MSE"],
            }
        ],
        "rnas": [],
        "dnas": [],
        "carbs": [],
        "ligands": [],
        "buffers": [],
    }
    _test_contents("1o6a", expected, selenomet=True)


def test_4gxy():
    expected = {
        "copies": 1,
        "proteins": [],
        "rnas": [
            {
                "sequence": "GGCGGCAGGUGCUCCCGACCCUGCGGUCGGGAGUUAAAAGGGAAGCCGGUGCAAGUCCGGCACGGUCCCGCCACUGUGACGGGGAGUCGCCCCUCGGGAUGUGCCACUGGCCCGAAGGCCGGGAAGGCGGAGGGGCGGCGAGGAUCCGGAGUCAGGAAACCUGCCUGCCGUC",
                "start": 1,
                "copies": 1,
                "modifications": ["1->GTP", "172->CCC"],
            }
        ],
        "dnas": [],
        "carbs": [],
        "ligands": [
            {"code": "B1Z", "copies": 2},
            {"code": "IRI", "copies": 7},
        ],
        "buffers": ["MG"],
    }
    _test_contents("4gxy", expected, selenomet=False)


def test_6as7():
    expected = {
        "copies": 1,
        "proteins": [
            {
                "sequence": "DEEQVFHFYWLDAYEDQYNQPGVVFLFGKVWIESAETHVSCCVMVKNIERTLYFLPREMKIDLNTGKETGTPISMKDVYEEFDEKIATKYKIMKFKSKPVEKNYAFEIPDVPEKSEYLEVKYSAEMPQLPQDLKGETFSHVFGTNTSSLELFLMNRKIKGPCWLEVKSPQLLNQPVSWCKAEAMALKPDLVNVIKDVSPPPLVVMAFSMKTMQNAKNHQNEIIAMAALVHHSFALDKAAPKPPFQSHFCVVSKPKDCIFPYAFKEVIEKKNVKVEVAATERTLLGFFLAKVHKIDPDIIVGHNIYGFELEVLLQRINVCKAPHWSKIGRLKRSNMPKLGGRSGFGERNATCGRMICDVEISAKELIRCKSYHLSELVQQILKTERVVIPMENIQNMYSESSQLLYLLEHTWKDAKFILQIMCELNVLPLALQITNIAGNIMSRTLMGGRSERNEFLLLHAFYENNYIVPDKQIFRKPQQKLGDEDEEIDGDTNKYKKGRKKAAYAGGLVLDPKVGFYDKFILLLDFNSLYPSIIQEFNICFTTVQRVASEAQKVTEDGEQEQIPELPDPSLEMGILPREIRKLVERRKQVKQLMKQQDLNPDLILQYDIRQKALKLTANSMYGCLGFSYSRFYAKPLAALVTYKGREILMHTKEMVQKMNLEVIYGDTDSIMINTNSTNLEEVFKLGNKVKSEVNKLYKLLEIDIDGVFKSLLLLKKKKYAALVVEPTSDGNYVTKQELKGLDIVRRDWCDLAKDTGNFVIGQILSDQSRDTIVENIQKRLIEIGENVLNGSVPVSQFEINKALTKDPQDYPDKKSLPHVHVALWINSQGGRKVKAGDTVSYVICQDGSNLTASQRAYAPEQLQKQDNLTIDTQYYLAQQIHPVVARICEPIDGIDAVLIATWLGLDPTQFRVHHYHKDEEN",
                "start": 1,
                "copies": 1,
                "modifications": [],
            }
        ],
        "rnas": [],
        "dnas": [
            {
                "sequence": "GCCTGGAGCGC",
                "start": 1,
                "copies": 1,
                "modifications": [],
            },
            {
                "sequence": "AGGCGCTCCAGGC",
                "start": 1,
                "copies": 1,
                "modifications": [],
            },
        ],
        "carbs": [],
        "ligands": [{"code": "DCP", "copies": 1}],
        "buffers": ["MG", "CO"],
    }
    _test_contents("6as7", expected, selenomet=False)


def test_4aqd():
    expected = {
        "copies": 1,
        "proteins": [
            {
                "sequence": "RSEDDIIIATKNGKVRGMNLTVFGGTVTAFLGIPYAQPPLGRLRFKKPQSLTKWSDIWNATKYANSCCQNIDQSFPGFHGSEMWNPNTDLSEDCLYLNVWIPAPKPKNATVLIWIYGGGFQTGTSSLHVYDGKFLARVERVIVVSMNYRVGALGFLALPGNPEAPGNMGLFDQQLALQWVQKNIAAFGGNPKSVTLFGESAGAASVSLHLLSPGSHSLFTRAILQSGSFNAPWAVTSLYEARNRTLNLAKLTGCSRENETEIIKCLRNKDPQEILLNEAFVVPYGTPLSVNFGPTVDGDFLTDMPDILLELGQFKKTQILVGVNKDEGTAFLVYGAPGFSKDNNSIITRKEFQEGLKIFFPGVSEFGKESILFHYTDWVDDQRPENYREALGDVVGDYNFICPALEFTKKFSEWGNNAFFYYFEHRSSKLPWPEWMGVMHGYEIEFVFGLPLERRDNYTKAEEILSRSIVKRWANFAKYGNPNETQNNSTSWPVFKSTEQKYLTLNTESTRIMTKLRAQQCRFWTSFFPKV",
                "start": 1,
                "copies": 2,
                "modifications": [],
            }
        ],
        "rnas": [],
        "dnas": [],
        "carbs": [
            {"codes": {"NAG": 2}, "copies": 2},
            {"codes": {"FUL": 1, "NAG": 2}, "copies": 6},
            {"codes": {"MAN": 1, "NAG": 2}, "copies": 1},
        ],
        "ligands": [
            {"code": "BAL", "copies": 2},
            {"code": "NAG", "copies": 6},
            {"code": "PG4", "copies": 2},
            {"code": "PEG", "copies": 2},
        ],
        "buffers": ["EDO", "CL", "GLY"],
    }
    _test_contents("4aqd", expected, selenomet=False)


def test_1vjr():
    expected = {
        "copies": 1,
        "proteins": [
            {
                "sequence": "MGSDKIHHHHHHVLDKIELFILDMDGTFYLDDSLLPGSLEFLETLKEKNKRFVFFTNNSSLGAQDYVRKLRNMGVDVPDDAVVTSGEITAEHMLKRFGRCRIFLLGTPQLKKVFEAYGHVIDEENPDFVVLGFDKTLTYERLKKACILLRKGKFYIATHPDINCPSKEGPVPDAGSIMAAIEASTGRKPDLIAGKPNPLVVDVISEKFGVPKERMAMVGDRLYTDVKLGKNAGIVSILVLTGETTPEDLERAETKPDFVFKNLGELAKAVQ",
                "start": 1,
                "copies": 1,
                "modifications": ["M->MSE"],
            }
        ],
        "rnas": [],
        "dnas": [],
        "carbs": [],
        "ligands": [],
        "buffers": ["NI", "CL"],
    }
    _test_contents("1vjr", expected, selenomet=True)


def test_1cag():
    expected = {
        "copies": 3,
        "proteins": [
            {
                "sequence": "PPGPPGPPGPPGPPAPPGPPGPPGPPGPPG",
                "start": 1,
                "copies": 1,
                "modifications": [
                    "2->HYP",
                    "5->HYP",
                    "8->HYP",
                    "11->HYP",
                    "14->HYP",
                    "17->HYP",
                    "20->HYP",
                    "23->HYP",
                    "26->HYP",
                    "29->HYP",
                ],
            }
        ],
        "rnas": [],
        "dnas": [],
        "carbs": [],
        "ligands": [],
        "buffers": ["ACY"],
    }
    contents = _test_contents("1cag", expected, selenomet=False)
    polymer = contents.proteins[0]
    codes = polymer.residue_codes()
    ppg = ["PRO", "HYP", "GLY"]
    ppa = ["PRO", "HYP", "ALA"]
    assert codes == ppg * 4 + ppa + ppg * 5

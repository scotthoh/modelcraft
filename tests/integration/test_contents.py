from modelcraft.contents import AsuContents


def _test_contents(pdbid: str, expected: list, selenomet: bool):
    contents = AsuContents(pdbid)
    assert contents.components_json() == expected
    assert contents.is_selenomet() == selenomet


def test_1o6a():
    expected = [
        {
            "sequence": "SETRKTEVPSDKLELLLDIPLKVTVELGRTRMTLKRVLEMIHGSIIELDKLTGEPVDILVNGKLIARGEVVVIDENFGVRITEIVSPKERLELLNE",
            "type": "PROTEIN",
            "start": 1,
            "copies": 2,
            "modifications": ["M->MSE"],
        }
    ]
    _test_contents("1o6a", expected, selenomet=True)


def test_4gxy():
    expected = [
        {
            "sequence": "GGCGGCAGGUGCUCCCGACCCUGCGGUCGGGAGUUAAAAGGGAAGCCGGUGCAAGUCCGGCACGGUCCCGCCACUGUGACGGGGAGUCGCCCCUCGGGAUGUGCCACUGGCCCGAAGGCCGGGAAGGCGGAGGGGCGGCGAGGAUCCGGAGUCAGGAAACCUGCCUGCCGUC",
            "type": "RNA",
            "start": 1,
            "copies": 1,
            "modifications": ["1->GTP", "172->CCC"],
        },
        {"code": "B1Z", "copies": 2},
        {"code": "IRI", "copies": 7},
        {"code": "MG", "copies": 2},
    ]
    _test_contents("4gxy", expected, selenomet=False)


def test_6as7():
    expected = [
        {
            "sequence": "DEEQVFHFYWLDAYEDQYNQPGVVFLFGKVWIESAETHVSCCVMVKNIERTLYFLPREMKIDLNTGKETGTPISMKDVYEEFDEKIATKYKIMKFKSKPVEKNYAFEIPDVPEKSEYLEVKYSAEMPQLPQDLKGETFSHVFGTNTSSLELFLMNRKIKGPCWLEVKSPQLLNQPVSWCKAEAMALKPDLVNVIKDVSPPPLVVMAFSMKTMQNAKNHQNEIIAMAALVHHSFALDKAAPKPPFQSHFCVVSKPKDCIFPYAFKEVIEKKNVKVEVAATERTLLGFFLAKVHKIDPDIIVGHNIYGFELEVLLQRINVCKAPHWSKIGRLKRSNMPKLGGRSGFGERNATCGRMICDVEISAKELIRCKSYHLSELVQQILKTERVVIPMENIQNMYSESSQLLYLLEHTWKDAKFILQIMCELNVLPLALQITNIAGNIMSRTLMGGRSERNEFLLLHAFYENNYIVPDKQIFRKPQQKLGDEDEEIDGDTNKYKKGRKKAAYAGGLVLDPKVGFYDKFILLLDFNSLYPSIIQEFNICFTTVQRVASEAQKVTEDGEQEQIPELPDPSLEMGILPREIRKLVERRKQVKQLMKQQDLNPDLILQYDIRQKALKLTANSMYGCLGFSYSRFYAKPLAALVTYKGREILMHTKEMVQKMNLEVIYGDTDSIMINTNSTNLEEVFKLGNKVKSEVNKLYKLLEIDIDGVFKSLLLLKKKKYAALVVEPTSDGNYVTKQELKGLDIVRRDWCDLAKDTGNFVIGQILSDQSRDTIVENIQKRLIEIGENVLNGSVPVSQFEINKALTKDPQDYPDKKSLPHVHVALWINSQGGRKVKAGDTVSYVICQDGSNLTASQRAYAPEQLQKQDNLTIDTQYYLAQQIHPVVARICEPIDGIDAVLIATWLGLDPTQFRVHHYHKDEEN",
            "type": "PROTEIN",
            "start": 1,
            "copies": 1,
            "modifications": [],
        },
        {
            "sequence": "GCCTGGAGCGC",
            "type": "DNA",
            "start": 1,
            "copies": 1,
            "modifications": [],
        },
        {
            "sequence": "AGGCGCTCCAGGC",
            "type": "DNA",
            "start": 1,
            "copies": 1,
            "modifications": [],
        },
        {"code": "DCP", "copies": 1},
        {"code": "MG", "copies": 2},
        {"code": "CO", "copies": 2},
    ]
    _test_contents("6as7", expected, selenomet=False)


def test_4aqd():
    expected = [
        {
            "sequence": "RSEDDIIIATKNGKVRGMNLTVFGGTVTAFLGIPYAQPPLGRLRFKKPQSLTKWSDIWNATKYANSCCQNIDQSFPGFHGSEMWNPNTDLSEDCLYLNVWIPAPKPKNATVLIWIYGGGFQTGTSSLHVYDGKFLARVERVIVVSMNYRVGALGFLALPGNPEAPGNMGLFDQQLALQWVQKNIAAFGGNPKSVTLFGESAGAASVSLHLLSPGSHSLFTRAILQSGSFNAPWAVTSLYEARNRTLNLAKLTGCSRENETEIIKCLRNKDPQEILLNEAFVVPYGTPLSVNFGPTVDGDFLTDMPDILLELGQFKKTQILVGVNKDEGTAFLVYGAPGFSKDNNSIITRKEFQEGLKIFFPGVSEFGKESILFHYTDWVDDQRPENYREALGDVVGDYNFICPALEFTKKFSEWGNNAFFYYFEHRSSKLPWPEWMGVMHGYEIEFVFGLPLERRDNYTKAEEILSRSIVKRWANFAKYGNPNETQNNSTSWPVFKSTEQKYLTLNTESTRIMTKLRAQQCRFWTSFFPKV",
            "type": "PROTEIN",
            "start": 1,
            "copies": 2,
            "modifications": [],
        },
        {"codes": {"NAG": 2}, "copies": 2},
        {"codes": {"FUL": 1, "NAG": 2}, "copies": 6},
        {"codes": {"MAN": 1, "NAG": 2}, "copies": 1},
        {"code": "BAL", "copies": 2},
        {"code": "NAG", "copies": 6},
        {"code": "PG4", "copies": 2},
        {"code": "EDO", "copies": 19},
        {"code": "CL", "copies": 7},
        {"code": "GLY", "copies": 2},
        {"code": "PEG", "copies": 2},
    ]
    _test_contents("4aqd", expected, selenomet=False)


def test_1vjr():
    expected = [
        {
            "sequence": "MGSDKIHHHHHHVLDKIELFILDMDGTFYLDDSLLPGSLEFLETLKEKNKRFVFFTNNSSLGAQDYVRKLRNMGVDVPDDAVVTSGEITAEHMLKRFGRCRIFLLGTPQLKKVFEAYGHVIDEENPDFVVLGFDKTLTYERLKKACILLRKGKFYIATHPDINCPSKEGPVPDAGSIMAAIEASTGRKPDLIAGKPNPLVVDVISEKFGVPKERMAMVGDRLYTDVKLGKNAGIVSILVLTGETTPEDLERAETKPDFVFKNLGELAKAVQ",
            "type": "PROTEIN",
            "start": 1,
            "copies": 1,
            "modifications": ["M->MSE"],
        },
        {"code": "NI", "copies": 1},
        {"code": "CL", "copies": 2},
    ]
    _test_contents("1vjr", expected, selenomet=True)


def test_1cag():
    expected = [
        {
            "sequence": "PPGPPGPPGPPGPPAPPGPPGPPGPPGPPG",
            "type": "PROTEIN",
            "start": 1,
            "copies": 3,
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
        },
        {"code": "ACY", "copies": 6},
    ]
    _test_contents("1cag", expected, selenomet=False)

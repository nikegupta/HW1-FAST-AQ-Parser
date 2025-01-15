# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)



def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    fp = FastaParser('data/test.fa')
    record_list = []
    for record in fp:
        record_list.append(record)

    assert record_list[0] == ('seq0', 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA')
    assert record_list[1] == ('seq1', 'TCCGCCCGCTGTGCTGACGAGACTAGCAGGGAAATAAATAGAGGGTTTAGTTATACTCAGTAGGCAGTTCGATGGCTTATATCTAACTTCTTATTCCGAT')

    error = False
    fp = FastaParser('tests/bad.fa')
    try:
        for record in fp:
            pass
    except ValueError:
        error = True
    else:
        pass
    assert error == True

    error = False
    fp = FastaParser('tests/blank.fa')
    try:
        for record in fp:
            pass
    except ValueError:
        error = True
    else:
        pass
    assert error == True
        
  

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """

    fp = FastaParser('data/test.fq')
    record_list = []
    for record in fp:
        record_list.append(record)

    assert record_list[0][0] == None
    assert record_list[1][0] == None


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """

    fqp = FastqParser('data/test.fq')
    record_list = []
    for record in fqp:
        record_list.append(record)

    assert record_list[0] == ('seq0', 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG', '*540($=*,=.062565,2>\'487\')!:&&6=,6,*7>:&132&83*8(58&59>\'8!;28<94,0*;*.94**:9+7\"94(>7=\'(!5\"2/!%\"4#32=')
    assert record_list[1] == ('seq1', 'CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGGCAAGCAGACCCATATCGTCCTGCTGGCAACGCTATCCGGGTGCGAGTAAATCGAAACCTCG', '\'(<#/0$5&!$+,:=%7=50--1;\'(-7;0>=$(05*9,,:%0!<),%646<8#%\".\"-\'*-0:.+*&$5!\'8)(%3*+9/&/%=363*,6$20($97,\"')

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fqp = FastqParser('data/test.fa')
    record_list = []
    for record in fqp:
        record_list.append(record)

    assert record_list[0][0] == None
    assert record_list[1][0] == None

import pytest
import ffp
import json

#yes I am aware there is some redundancy in these tests but they allow for more specific debugging

class TestClass:
    
    def test_default(self):
        #test using default spec
        #exact sized words
        config = "config/spec.json"
        cfg = ffp.readConfig(config)
        
        input = "input/test1.in"
        output = "output/test1.out"
        testdata = "testdata/test1.csv"
        
        
        ffp.parse(config, input, output)
        src = ffp.readCSV(output, cfg['DelimitedEncoding'] ,cfg["IncludeHeader"])
        tgt = ffp.readCSV(testdata, cfg['DelimitedEncoding'], cfg["IncludeHeader"])
        
        assert src == tgt
    
    def test_whitespace_header(self):
        #remove whitespaces
        #header off
        config = "config/test2.json"
        cfg = ffp.readConfig(config)
        
        input = "input/test2.in"
        output = "output/test2.out"
        testdata = "testdata/test2.csv"
        
        
        ffp.parse(config, input, output)
        src = ffp.readCSV(output, cfg['DelimitedEncoding'] ,cfg["IncludeHeader"])
        tgt = ffp.readCSV(testdata, cfg['DelimitedEncoding'], cfg["IncludeHeader"])
        
        assert src == tgt

    def test_header_on(self):
        #test header on
        config = "config/test3.json"
        cfg = ffp.readConfig(config)
        
        input = "input/test3.in"
        output = "output/test3.out"
        testdata = "testdata/test3.csv"
        
        
        ffp.parse(config, input, output)
        src = ffp.readCSV(output, cfg['DelimitedEncoding'], cfg["IncludeHeader"])
        tgt = ffp.readCSV(testdata, cfg['DelimitedEncoding'],cfg["IncludeHeader"])
        assert src == tgt
        
    def test_header_off(self):
        #test header off
        config = "config/test3a.json"
        cfg = ffp.readConfig(config)
        
        input = "input/test3.in"
        output = "output/test3a.out"
        testdata = "testdata/test3a.csv"
        
        
        ffp.parse(config, input, output)
        src = ffp.readCSV(output, cfg['DelimitedEncoding'], cfg["IncludeHeader"])
        tgt = ffp.readCSV(testdata, cfg['DelimitedEncoding'],cfg["IncludeHeader"])
        assert src == tgt

    def test_encoding_1(self):
        #wrong read decoding, src file has UTF-8 japanese characters
        
        with pytest.raises(UnicodeDecodeError):
            config = "config/spec.json"
            cfg = ffp.readConfig(config)
        
            input = "input/test6.in"
            output = "output/test6.out"
            testdata = "testdata/test6.csv"
        
        
            ffp.parse(config, input, output)
            src = ffp.readCSV(output, cfg['DelimitedEncoding'], cfg["IncludeHeader"])
            tgt = ffp.readCSV(testdata, cfg['DelimitedEncoding'],cfg["IncludeHeader"])
            assert src == tgt

    def test_encoding_2(self):
        #wrong read encoding, tgt file has UTF-8 japanese characters
        
        with pytest.raises(UnicodeEncodeError):
            config = "config/spec2.json"
            cfg = ffp.readConfig(config)
        
            input = "input/test6.in"
            output = "output/test6.out"
            testdata = "testdata/test6.csv"
        
        
            ffp.parse(config, input, output)
            src = ffp.readCSV(output, cfg['DelimitedEncoding'], cfg["IncludeHeader"])
            tgt = ffp.readCSV(testdata, cfg['DelimitedEncoding'],cfg["IncludeHeader"])
            assert src == tgt
       
    def test_encoding_3(self):
        #wrong read encoding, tgt file has UTF-8 japanese characters
        
        config = "config/spec3.json"
        cfg = ffp.readConfig(config)
        
        input = "input/test6.in"
        output = "output/test6.out"
        testdata = "testdata/test6.csv"
        
        
        ffp.parse(config, input, output)
        src = ffp.readCSV(output, cfg['DelimitedEncoding'], cfg["IncludeHeader"])
        tgt = ffp.readCSV(testdata, cfg['DelimitedEncoding'],cfg["IncludeHeader"])
        assert src == tgt
        
    def test_commas(self):
        #test commas in data
        config = "config/test3.json"
        cfg = ffp.readConfig(config)
        
        input = "input/test4.in"
        output = "output/test4.out"
        testdata = "testdata/test4comma.csv"
        
        
        ffp.parse(config, input, output)
        src = ffp.readCSV(output, cfg['DelimitedEncoding'], cfg["IncludeHeader"])
        tgt = ffp.readCSV(testdata, cfg['DelimitedEncoding'],cfg["IncludeHeader"])
        assert src == tgt
        
    def test_trunc(self):
        #test truncated field
        config = "config/test3.json"
        cfg = ffp.readConfig(config)
        
        input = "input/test5.in"
        output = "output/test5.out"
        testdata = "testdata/test5.csv"
        
        
        ffp.parse(config, input, output)
        src = ffp.readCSV(output, cfg['DelimitedEncoding'], cfg["IncludeHeader"])
        tgt = ffp.readCSV(testdata, cfg['DelimitedEncoding'],cfg["IncludeHeader"])
        assert src == tgt
    
    def test_ws(self):
        #remove whitespaces
        config = "config/winter_soldier.json"
        cfg = ffp.readConfig(config)
        
        input = "input/winter_soldier.in"
        output = "output/winter_soldier.out"
        testdata = "testdata/winter_soldier.csv"
        
        
        ffp.parse(config, input, output)
        src = ffp.readCSV(output, cfg['DelimitedEncoding'])
        tgt = ffp.readCSV(testdata, cfg['DelimitedEncoding'])

        assert src == tgt
    
    def test_bad_config_1(self):
        #test bad config file column mismatch
        with pytest.raises(Exception):
            config = "config/cols.json"
            cfg = ffp.readConfig(config)
        
            input = "input/test5.in"
            output = "output/test5.out"
            testdata = "testdata/test5.csv"
        
        
            ffp.parse(config, input, output)
            src = ffp.readCSV(output, cfg['DelimitedEncoding'], cfg["IncludeHeader"])
            tgt = ffp.readCSV(testdata, cfg['DelimitedEncoding'],cfg["IncludeHeader"])
            assert src==tgt
    
    def test_bad_config_2(self):
        #test bad config file column mismatch
        with pytest.raises(json.decoder.JSONDecodeError):
            config = "config/bad_config.json"
            cfg = ffp.readConfig(config)
        
            input = "input/test5.in"
            output = "output/test5.out"
            testdata = "testdata/test5.csv"
        
        
            ffp.parse(config, input, output)
            src = ffp.readCSV(output, cfg['DelimitedEncoding'], cfg["IncludeHeader"])
            tgt = ffp.readCSV(testdata, cfg['DelimitedEncoding'],cfg["IncludeHeader"])
            assert src==tgt
    
    def test_newline(self):
        #test commas in data
        config = "config/test3.json"
        cfg = ffp.readConfig(config)
        
        input = "input/test7.in"
        output = "output/test7.out"
        testdata = "testdata/test7.csv"
        
        
        ffp.parse(config, input, output)
        src = ffp.readCSV(output, cfg['DelimitedEncoding'], cfg["IncludeHeader"])
        tgt = ffp.readCSV(testdata, cfg['DelimitedEncoding'],cfg["IncludeHeader"])
        assert src == tgt
        
    def test_config_file_not_found(self):
        #test filename not found
        with pytest.raises(FileNotFoundError):
            config = "config/co!!!ls.json"
            cfg = ffp.readConfig(config)
        
            input = "input/test5.in"
            output = "output/test5.out"
            testdata = "testdata/test5.csv"
        
        
            ffp.parse(config, input, output)
            src = ffp.readCSV(output, cfg['DelimitedEncoding'], cfg["IncludeHeader"])
            tgt = ffp.readCSV(testdata, cfg['DelimitedEncoding'],cfg["IncludeHeader"])
            assert src==tgt
            
    def test_src_file_not_found(self):
        #test filename not found
        with pytest.raises(Exception):
            config = "config/test3.json"
            cfg = ffp.readConfig(config)
        
            input = "input/BLARGH.in"
            output = "output/test5.out"
            testdata = "testdata/test5.csv"
        
        
            ffp.parse(config, input, output)
            src = ffp.readCSV(output, cfg['DelimitedEncoding'], cfg["IncludeHeader"])
            tgt = ffp.readCSV(testdata, cfg['DelimitedEncoding'],cfg["IncludeHeader"])
            assert src==tgt
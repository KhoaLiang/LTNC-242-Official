import unittest
from TestUtils import TestUtils


class TestSymbolTable(unittest.TestCase):
    def test_0(self):
        input = ["INSERT a1 number", "INSERT b2 string"]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 100))

    def test_1(self):
        input = ["INSERT x number", "INSERT y string", "INSERT x string"]
        expected = ["Redeclared: INSERT x string"]

        self.assertTrue(TestUtils.check(input, expected, 101))
    
    # TypeMismatch error for assign
    def test_2(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x 15",
            "ASSIGN y 17",
            "ASSIGN x 'abc'",
        ]
        expected = ["TypeMismatch: ASSIGN y 17"]

        self.assertTrue(TestUtils.check(input, expected, 102))


    def test_4(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "LOOKUP x",
            "LOOKUP y",
            "END",
        ]
        expected = ["success", "success", "success", "1", "0"]

        self.assertTrue(TestUtils.check(input, expected, 104))

    def test_5(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT z number",
            "PRINT",
            "END",
        ]
        expected = ["success", "success", "success", "success", "y//0 x//1 z//1"]

        self.assertTrue(TestUtils.check(input, expected, 105))

    def test_6(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT z number",
            "RPRINT",
            "END",
        ]
        expected = ["success", "success", "success", "success", "z//1 x//1 y//0"]

        self.assertTrue(TestUtils.check(input, expected, 106))
    def test_7(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x 15",
            "ASSIGN y 'nannikure'",
            "ASSIGN x 'abc'",
        ]
        expected = ["TypeMismatch: ASSIGN x 'abc'"]

        self.assertTrue(TestUtils.check(input, expected, 107))
    # Undeclared error for assign
    def test_8(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x 15",
            "ASSIGN y 'nannikure'",
            "ASSIGN z 'abc'",
        ]
        expected = ["Undeclared: ASSIGN z 'abc'"]

        self.assertTrue(TestUtils.check(input, expected, 108))
    def test_9(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN x 15",
            "ASSIGN y 'nannikure'",
            "ASSIGN w z",
        ]
        expected = ["Undeclared: ASSIGN w z"]

        self.assertTrue(TestUtils.check(input, expected, 109))
    def test_10(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN x 15",
            "ASSIGN y 'nannikure'",
            "ASSIGN t x",
        ]
        expected = ["Undeclared: ASSIGN t x"]

        self.assertTrue(TestUtils.check(input, expected, 110))
    
    # white space and valid declaration error for insert
    def test_11(self):
        input = [
            "  INSERT x number",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN x 15",
            "ASSIGN y 'nannikure'",
        ]
        expected = ["InvalidInstruction:   INSERT x number"]

        self.assertTrue(TestUtils.check(input, expected, 111))
    def test_12(self):
        input = [
            "INSERT x    number",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN x 15",
            "ASSIGN y 'nannikure'",
        ]
        expected = ["InvalidInstruction: INSERT x    number"]
        self.assertTrue(TestUtils.check(input, expected, 112))
    def test_13(self):
        input = [
            "INSERT     x number",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN x 15",
            "ASSIGN y 'nannikure'",
        ]
        expected = ["InvalidInstruction: INSERT     x number"]
        self.assertTrue(TestUtils.check(input, expected, 113))
    def test_14(self):
        input = [
            "INSERT x number  ",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN x 15",
            "ASSIGN y 'nannikure'",
        ]
        expected = ["InvalidInstruction: INSERT x number  "]
        self.assertTrue(TestUtils.check(input, expected, 114))
    def test_15(self):
        input = [
            "INSERT x",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN x 15",
            "ASSIGN y 'nannikure'",
        ]
        expected = ["InvalidInstruction: INSERT x"]
        self.assertTrue(TestUtils.check(input, expected, 115))
    def test_16(self):
        input = [
            "INSERT string",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN x 15",
            "ASSIGN y 'nannikure'",
        ]
        expected = ["InvalidInstruction: INSERT string"]
        self.assertTrue(TestUtils.check(input, expected, 116))
    
    # White space and valid declaration error for assign
    def test_17(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "INSERT w string",
            "  ASSIGN x 15",
            "ASSIGN y 'nannikure'",
        ]
        expected = ["InvalidInstruction:   ASSIGN x 15"]
        self.assertTrue(TestUtils.check(input, expected, 117))

    def test_18(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN   x 15",
            "ASSIGN y 'nannikure'",
        ]
        expected = ["InvalidInstruction: ASSIGN   x 15"]
        self.assertTrue(TestUtils.check(input, expected, 118))

    def test_19(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN x    15",
            "ASSIGN y 'nannikure'",
        ]
        expected = ["InvalidInstruction: ASSIGN x    15"]
        self.assertTrue(TestUtils.check(input, expected, 119))

    def test_20(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN x 15  ",
            "ASSIGN y 'nannikure'",
        ]
        expected = ["InvalidInstruction: ASSIGN x 15  "]
        self.assertTrue(TestUtils.check(input, expected, 120))

    def test_21(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN x",
            "ASSIGN y 'nannikure'",
        ]
        expected = ["InvalidInstruction: ASSIGN x"]
        self.assertTrue(TestUtils.check(input, expected, 121))

    def test_22(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN",
            "ASSIGN y 'nannikure'",
        ]
        expected = ["InvalidInstruction: ASSIGN"]
        self.assertTrue(TestUtils.check(input, expected, 122))
    def test_23(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN string",
            "ASSIGN y 'nannikure'",
        ]
        expected = ["InvalidInstruction: ASSIGN string"]
        self.assertTrue(TestUtils.check(input, expected, 123))
    def test_24(self):
        input = [
            "INSERT xMe_3 number",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN xMe_3 34",
            "ASSIGN y 'nanni_kure'",
        ]
        expected = ["InvalidInstruction: ASSIGN y 'nanni_kure'"]
        self.assertTrue(TestUtils.check(input, expected, 124))
    def test_25(self):
        input = [
            "INSERT xMe_3 number",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN xMe_3 34.4",
            "ASSIGN y 'nanni'",
        ]
        expected = ["InvalidInstruction: ASSIGN xMe_3 34.4"]
        self.assertTrue(TestUtils.check(input, expected, 125))
    def test_26(self):
        input = [
            "INSERT xMe_3 number",
            "INSERT y string",
            "INSERT w string",
            "ASSIGN xMe_3 34",
        ]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 126))
    def test_27(self):
        input = [
            "INSERT xMe_3 number",
            "INSERT y number",
            "ASSIGN y 36",
            "ASSIGN xMe_3 y",
        ]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 127))
    # TypeMismatch error
    def test_28(self):
        input = [
            "INSERT xMe_3 number",
            "INSERT y string",
            "ASSIGN y 'hello'",
            "ASSIGN xMe_3 y",
        ]
        expected = ["TypeMismatch: ASSIGN xMe_3 y"]
        self.assertTrue(TestUtils.check(input, expected, 128))
    
    # Block test
    def test_3(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "BEGIN",
            "INSERT y string",
            "END",
            "END",
        ]
        expected = ["success", "success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 103))
    def test_29(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "BEGIN",
            "INSERT y string",
            "END",
        ]
        expected = ["UnclosedBlock: 1"]

        self.assertTrue(TestUtils.check(input, expected, 129))
    def test_30(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "BEGIN",
            "INSERT y string",
        ]
        expected = ["UnclosedBlock: 2"]

        self.assertTrue(TestUtils.check(input, expected, 130))
    def test_31(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT y string",
            "END",
            "END",
        ]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 131))
    # test print
    def test_32(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT xx number",
            "INSERT zz number",
            "INSERT ww number",
            "BEGIN",
            "INSERT uuu number",
            "INSERT ttt number",
            "INSERT vvv number",
            "PRINT",
            "END",
            "END",
        ]
        expected = ["success", "success", "success", "success", "success", "success", "success", "success", "x//0 y//0 xx//1 zz//1 ww//1 uuu//2 ttt//2 vvv//2"]

        self.assertTrue(TestUtils.check(input, expected, 132))
    def test_33(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "INSERT z number",
            "BEGIN",
            "INSERT x number",
            "INSERT y number",
            "PRINT",
            "END",
        ]
        expected = ["success", "success", "success", "success", "success", "z//0 x//1 y//1"]

        self.assertTrue(TestUtils.check(input, expected, 133))
    # test reprint
    def test_34(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT y number",
            "INSERT z number",
            "RPRINT",
            "END",
        ]
        expected = ["success", "success", "success", "success", "z//1 y//1 x//0"]

        self.assertTrue(TestUtils.check(input, expected, 134))
    def test_35(self):
        input = [
            "INSERT a number",
            "INSERT b string",
            "BEGIN",
            "INSERT c number",
            "INSERT d string",
            "RPRINT",
            "END",
        ]
        expected = ["success", "success", "success", "success", "d//1 c//1 b//0 a//0"]

        self.assertTrue(TestUtils.check(input, expected, 135))

    def test_36(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT y string",
            "PRINT",
            "END",
        ]
        expected = ["success", "success", "success", "success", "x//1 y//1"]

        self.assertTrue(TestUtils.check(input, expected, 136))

    def test_37(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "BEGIN",
            "INSERT w string",
            "RPRINT",
            "END",
            "END",
        ]
        expected = ["success", "success", "success", "success", "w//2 z//1 y//0 x//0"]

        self.assertTrue(TestUtils.check(input, expected, 137))

    def test_38(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "BEGIN",
            "INSERT w string",
            "END",
            "PRINT",
            "END",
        ]
        expected = ["success", "success", "success", "success", "success", "z//1 y//0 x//0"]

        self.assertTrue(TestUtils.check(input, expected, 138))

    def test_39(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "BEGIN",
            "INSERT w string",
            "END",
            "END",
            "PRINT",
        ]
        expected = ["success", "success", "success", "success", "x//0 y//0"]

        self.assertTrue(TestUtils.check(input, expected, 139))

    def test_40(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "BEGIN",
            "INSERT w string",
            "END",
            "END",
            "RPRINT",
        ]
        expected = ["success", "success", "success", "success", "y//0 x//0"]

        self.assertTrue(TestUtils.check(input, expected, 140))

    def test_41(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "BEGIN",
            "INSERT w string",
            "END",
            "END",
            "LOOKUP x",
        ]
        expected = ["success", "success", "success", "success", "0"]

        self.assertTrue(TestUtils.check(input, expected, 141))

    def test_42(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "BEGIN",
            "INSERT w string",
            "END",
            "END",
            "LOOKUP z",
        ]
        expected = ["Undeclared: LOOKUP z"]

        self.assertTrue(TestUtils.check(input, expected, 142))

    def test_43(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "BEGIN",
            "INSERT w string",
            "END",
            "END",
            "LOOKUP w",
        ]
        expected = ["Undeclared: LOOKUP w"]

        self.assertTrue(TestUtils.check(input, expected, 143))

    def test_44(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "BEGIN",
            "INSERT w string",
            "END",
            "END",
            "LOOKUP y",
        ]
        expected = ["success", "success", "success", "success", "0"]

        self.assertTrue(TestUtils.check(input, expected, 144))

    def test_45(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "BEGIN",
            "INSERT w string",
            "END",
            "END",
            "LOOKUP x",
        ]
        expected = ["success", "success", "success", "success", "success", "0"]

        self.assertTrue(TestUtils.check(input, expected, 145))

    def test_46(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "BEGIN",
            "INSERT w string",
            "END",
            "END",
            "LOOKUP z",
        ]
        expected = ["success", "success", "success", "success", "success", "Undeclared: LOOKUP z"]

        self.assertTrue(TestUtils.check(input, expected, 146))

    def test_47(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "BEGIN",
            "INSERT w string",
            "END",
            "END",
            "LOOKUP w",
        ]
        expected = ["success", "success", "success", "success", "success", "Undeclared: LOOKUP w"]

        self.assertTrue(TestUtils.check(input, expected, 147))

    def test_48(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "BEGIN",
            "INSERT w string",
            "END",
            "END",
            "LOOKUP y",
        ]
        expected = ["success", "success", "success", "success", "success", "0"]

        self.assertTrue(TestUtils.check(input, expected, 148))

    def test_49(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "BEGIN",
            "INSERT w string",
            "END",
            "END",
            "LOOKUP x",
        ]
        expected = ["success", "success", "success", "success", "success", "0"]

        self.assertTrue(TestUtils.check(input, expected, 149))

    def test_50(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "BEGIN",
            "INSERT w string",
            "END",
            "END",
            "LOOKUP z",
        ]
        expected = ["success", "success", "success", "success", "success", "Undeclared: LOOKUP z"]

        self.assertTrue(TestUtils.check(input, expected, 150))



    

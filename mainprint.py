
def mainprint(fileName, author, functionlist):
    if '' == author:
        author = 'wenjun'

    fp = open("Test_"+fileName+".c","w")
    fp.write('''
/* ***************************************************************************** **
**                                                                               **
**                AAA               BBBBBBBBBBBBBBBBB   BBBBBBBBBBBBBBBBB        **
**               A:::A              B::::::::::::::::B  B::::::::::::::::B       **
**              A:::::A             B::::::BBBBBB:::::B B::::::BBBBBB:::::B      **
**             A:::::::A            BB:::::B     B:::::BBB:::::B     B:::::B     **
**            A:::::::::A             B::::B     B:::::B  B::::B     B:::::B     **
**           A:::::A:::::A            B::::B     B:::::B  B::::B     B:::::B     **
**          A:::::A A:::::A           B::::BBBBBB:::::B   B::::BBBBBB:::::B      **
**         A:::::A   A:::::A          B:::::::::::::BB    B:::::::::::::BB       **
**        A:::::A     A:::::A         B::::BBBBBB:::::B   B::::BBBBBB:::::B      **
**       A:::::AAAAAAAAA:::::A        B::::B     B:::::B  B::::B     B:::::B     **
**      A:::::::::::::::::::::A       B::::B     B:::::B  B::::B     B:::::B     **
**     A:::::AAAAAAAAAAAAA:::::A      B::::B     B:::::B  B::::B     B:::::B     **
**    A:::::A             A:::::A   BB:::::BBBBBB::::::BBB:::::BBBBBB::::::B     **
**   A:::::A               A:::::A  B:::::::::::::::::B B:::::::::::::::::B      **
**  A:::::A                 A:::::A B::::::::::::::::B  B::::::::::::::::B       **
** AAAAAAA                   AAAAAAABBBBBBBBBBBBBBBBB   BBBBBBBBBBBBBBBBB        **
**                                                                               **
** ***************************************************************************** **
** ****************** COPYRIGHT (C) ABB-BOMEM INC, 2017 ************************ **
**                              GWR source code                                  **
** The information contained in this document has to be kept strictly            **
** confidential. Any unauthorized use, reproduction, distribution or             **
** disclosure to third parties is strictly forbidden. ABB reserves all           **
** rights regarding Intellectual Property Rights.                                **
**                                                                               **
** ***************************************************************************** **
** <fe_acquisition_test.c>                                                       **
**                                                                               **
** Developped for project GWR                                                    **
**                                                                               **
** Author(s):  Louis-David Coulombe, Software Engineering                    **
**                                                                               **
** ABB Inc.                                                                      **
** 3400, Rue Pierre-Ardouin                                                      **
** Quebec, Quebec G1P 0B2 CANADA                                                 **
**                                                                               **
** Phone: +1 418 877 2944                                                        **
** Fax:   +1 418 877 2834                                                        **
**<http://www.abb.com/analytical>                                                **
**                                                                               **
** ***************************************************************************** */
''')

    fp.write('''
//----------------------------------------------------------------
// Name of the test group, use the name of the file (without .c)
//----------------------------------------------------------------
''')
    fp.write("TEST_GROUP("+fileName+");")
    fp.write('''
    
//--------------------------------------------------------------------------------------------
// Tester of the test group, use the name of the file (without .c) and the name of the tester
//--------------------------------------------------------------------------------------------
''')
    fp.write("TEST_GROUP_TESTER("+fileName+","+author+");")
    fp.write('''
    
//----------------------------------------------------------------
// Add test to be run here
//----------------------------------------------------------------
''')
    fp.write("TEST_GROUP_RUNNER("+fileName+")\n{")
    fp.write('''
    
// Init
//RUN_TEST_CASE(sourcefile, function, testcase id);
''')
    for functionname in functionlist:
        functionname = functionname.split("(")[-2].split(" ")[-1]
        fp.write("    RUN_TEST_CASE("+fileName+","+functionname+",1);\n\n")

    fp.write("}")
    fp.write('''
    
//----------------------------------------------------------------
// Setup: Ran before each test in this group
//----------------------------------------------------------------
''')
    fp.write("TEST_SETUP("+fileName+")\n{\n}")

    fp.write('''
    
    
//----------------------------------------------------------------
// Tear down: Ran after each test in this group
//----------------------------------------------------------------
''')
    fp.write("TEST_TEAR_DOWN("+fileName+")\n{\n}")

    fp.write('''
    
    
//----------------------------------------------------------------
// Helper functions
//----------------------------------------------------------------
''')

    fp.write('''
    
    
//----------------------------------------------------------------
// Add all tests here
// Describe the test in the test name
//----------------------------------------------------------------
''')
    fp.write("TEST("+fileName+",FunctinonName,1)")
    fp.write('''
{

    
    /* Test case description. */
    AbbUnityPrintProcedure("1.");
    AbbUnityPrintCriteria("");
    
    /* Prepare test scenarios. */

    
    /* Run function under test. */

    
    /* Check test result. */
    TEST_ASSERT_EQUAL();
}
''')

    fp.close()
    return None

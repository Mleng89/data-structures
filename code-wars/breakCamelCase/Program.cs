/*
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
*/

static string BreakCamelCase(string str)
{
char[] strList = str.ToCharArray();
string result = "";

    foreach(char letter in strList){
        if(letter != char.ToUpper(letter)){
            result += letter.ToString();
        }
        else{
            result += " " + letter.ToString();
        }
    }
return result;
}


Console.WriteLine(BreakCamelCase("camelCasing")); // 'camel Casing'
Console.WriteLine(BreakCamelCase("camelCaseTesting")); // 'camel Case Testing'
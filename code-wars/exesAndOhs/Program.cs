/*
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
*/

static bool XO (string input){
char[] inputList = input.ToLower().ToCharArray();
int xCount = 0;
int oCount = 0;

foreach(char letter in inputList){
    if(letter == 'o'){
        oCount += 1;
    } else if(letter == 'x'){
        xCount +=1;
    }
}
return xCount == oCount;
}


Console.WriteLine(XO("xo")); // true
Console.WriteLine(XO("xxOo")); // true
Console.WriteLine(XO("xxxm")); // false
Console.WriteLine(XO("Oo")); //false
Console.WriteLine(XO("ooom")); // false
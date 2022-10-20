/*
Prompt
The goal of this exercise is to convert a string to a
new string where each character in the new string is "("
if that character appears only once in the original string,
or ")" if that character appears more than once in the
original string. Ignore capitalization when determining
if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
*/


static string DuplicateEncode(string word)
{
    string result = "";
    string unique = "(";
    string duplicate = ")";
    string lowerWord = word.ToLower();
    for (int i = 0; i < lowerWord.Length;i++){
        if(lowerWord.LastIndexOf(lowerWord[i]) == lowerWord.IndexOf(lowerWord[i])){
            result += unique;
        }
        else{
            result += duplicate;
        }
    }

    return result;
}

Console.WriteLine(DuplicateEncode("din"));  // "((("
Console.WriteLine(DuplicateEncode("recede"));  // "()()()"
Console.WriteLine(DuplicateEncode("Success"));  // ")())())"
Console.WriteLine(DuplicateEncode("(( @))"));  // "))(("

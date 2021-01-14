#include <iostream>
#include <cstdlib>
#include<ctime>
#include <string>
using namespace std;

int fillTheLetters (char, string, string&);

int main () {
    x :
    string name;
    char letter;
    string word;
    int tries=5;
    string countries[]={
            "afghanistan","albania","algeria","andorra","angola","argentina","armenia","australia","austria","azerbaijan",
            "bahamas","bahrain","bangladesh","barbados","belarus","belgium","belize","benin","bhutan","bolivia","botswana","brazil","bulgaria","burundi",
            "combodia","canada","chile","china","colombia","comoros","congo","cuba","cyprus",
            "denmark","dominica","djibouti",
            "ecuador","egypt","eritrea","estonia","eswatini","ethopia",
            "fiji","finland","france",
            "gabon","gambia","georgia","germany","greece","guinea","guyana",
            "haiti","hungary","honduras",
            "iceland","india","indonesia","iran","iraq","ireland","israel","italy",
            "jamaica","japan","jordan",
            "kazakhstan","kenya","kiribati","kuwait","kyrgyzstan",
            "latvia","lebanon","lesotho","liberia","libya","lithuania",
            "madagascar","malawi","malaysia","maldives","mali","mexico","monaco","mongolia","montenegro","moroco","myanmar",
            "namibia","nauru","nepal","neitherlands","nicaragua","niger","nigeria","niue","norway",
            "oman",
            "pakistan","palau","panama","paraguay","peru","philippines","poland","portugal",
            "qatar",
            "romania","russia","rwanda",
            "serbia","samoa","senegal","singapore","slovenia","solomon","spain","suriname","sweden","switzerland",
            "tajikistan","thailand","tonga","tunisia","turkey","turkmenistan","tuvalu",
            "uganda","ukraine","uruguay","uzbekistan",
            "vanuatu","venezuela",
            "yemen",
            "zambia","zimbabwe"
    };
    srand(time(NULL));
    int n=rand()% 10;
    word=countries[n];
    string unknown(word.length(),'*');

    cout << "\n\nWelcome to Guessing Game.";
    cout << "\n\nGuess the Country Name and win exciting prices.";
    cout << "\n\nEach letter is represented by a star.";
    cout << "\n\nYou have to type only one letter in one try";
    cout << "\n\nYou have " << tries << " wrong tries to try and guess the word.";
    cout << "\n\nIf you guess wrong letter your tries will decrease";
    cout << "\n\nElse remain unchanged for a correct guess.";
    cout << "\n\nYou cannot guess the same letter twice.";
    cout << "\n\n----*----*----*----*----*----*----*----*----";
    while (tries) {
        cout << "\n\nWord to guess :- " << unknown;
        cout << "\n\nGuess a letter: ";
        cin >> letter;
        if (fillTheLetters(letter, word, unknown)==0) {
            cout << endl << "Oops! You have guessed the wrong letter!" << endl;
            tries=tries-1;
        }
        else {
            cout << endl << "Guessed letter is correct! Keep playing." << endl;
        }
        cout << "You have " << tries;
        cout << " wrong guesses left." << endl;
        if (word==unknown) {
            cout << word << endl;
            cout << "Yeah! You got it!";
            break;
        }
    }
    if(tries==0) {
        cout << "\nSorry, you lost the game" << endl;
        cout << "\nThe word was : " << word << endl;
    }
    cout<<"\n\nWould you like to play again?"<<endl;
    cout<<"y/n";
    char ch;
    cin>>ch;
    if(ch=='y' || ch=='Y') {
        goto x;
    }
    cin.ignore();
    cin.get();
    return 0;
}

int fillTheLetters (char guess, string secret_word, string &guess_the_word) {
    int i;
    int matches=0;
    for (i = 0; i< secret_word.length(); i++) {
        if (guess == guess_the_word[i]) {
            return 0;
        } else if (guess == secret_word[i]) {
            guess_the_word[i] = guess;
            matches++;
        }
    }
    return matches;
}
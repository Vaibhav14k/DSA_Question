#include<iostream>
using namespace std;
bool isvowles(char ch){
    if(ch =='a' || ch=='e' || ch=='i' || ch== 'o' || ch=='u'  ){
        return true;
    }else{
        return false;
    }
}
int main(){
    string s = "vaibhva";
    for(int i=0;i<s.length();i++){
        if(isvowles(s[i])){
            continue;
        }else{
            if( abs(s[i]) > 'a' &&  abs(s[i])<'e'   ){
                if(abs(s[i]-'a') > abs(s[i]-'e')){
                    s[i]='e';
                }else{
                    s[i]='a';
                }
            }else if ( abs(s[i])>'e' && abs(s[i])<'i'  ){
                if(abs(s[i]-'e') > abs(s[i]-'i') ){
                    s[i]='i';
                }else{
                    s[i]='e';
                }
            }
            else if ( abs(s[i])>'i' && abs(s[i])<'o'  ){
                if(abs(s[i]-'i') > abs(s[i]-'o') ){
                    s[i]='o';
                }else{
                    s[i]='i';
                }
            }
            else if ( abs(s[i])>'o' && abs(s[i])<'u'  ){
                if(abs(s[i]-'o') > abs(s[i]-'u') ){
                    s[i]='o';
                }else{
                    s[i]='u';
                }
            }
            else if (abs(s[i]) > 'u'  ){
                s[i]='u';
            }
        }
        // cout<<"newstring" << s;
    }
            cout<<"newstring" << endl<<s;

}
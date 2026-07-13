#include<iostream>
using namespace std;

// int countstring(string s){
//     int count=0;
//     for(char c : s){
//         // if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u' || c=='A' || c=='E' || c=='I' || c=='O' || c=='U') {
            
//         // }else{
//         //     count++;
//         // }
        
//     }
//     return count;
// }
int main(){
    string s = "hello";
    cout<<s.size();
    // cout<<countstring(s);
    for(int i=0;i<s.size();i++){
        int count =0;
        for(int j=i;j<s.size();j++){
            if(s[i] == s[j]){
                count++;
            }
        }
        cout<<"count for "<<s[i]<< " "<<count<<endl;
    }
}
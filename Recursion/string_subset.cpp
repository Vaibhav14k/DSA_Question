#include<iostream>
#include<vector>
using namespace std;
void subsets(string s,string ans,int i){
    if(i==s.size()){
        cout<<ans<<" ";
        cout<<endl;
        return;
    }
    subsets(s,ans + s[i]  ,i+1);
    subsets(s,ans,i+1);
}
int main() {
    string s = "ABC";
    subsets(s, "", 0);
}


// void generateBinary(int n, string s){
//     if(s.length() == n) {
//         cout << s << endl;
//         return;
//     } 
//     generateBinary(n,s+'0');
//     generateBinary(n,s+'1');
// };
// int main(){
//     int n=3;
//     generateBinary(n, "");
// }
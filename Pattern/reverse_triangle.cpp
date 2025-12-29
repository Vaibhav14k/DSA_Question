// #include<iostream>
// using namespace std;
// int main(){
//     for(int i=1;i<=4;i++){
//         for(int j=i;j>0;j--){
//             cout<<j;
//         }
//         cout<<endl;
//     }
// }
// 1
// 21
// 321
// 4321
#include<iostream>
using namespace std;
int main(){
    int num=0;
    for(int i=0;i<4;i++){
        for(int j=0;j<=i;j++){
            num=num+1;
            cout<<num;
        }
        cout<<endl;
    }
}

#include<iostream>
#include<map>
#include<unordered_map>
using namespace std;
int main(){
    unordered_map<string,int>m;
    m.emplace("vaibhav",23);
    m.emplace("samarth",24);
    m.emplace("sakshi",25);
    // for(auto p:m){
    //     cout<<p.first<<' '<<p.second;
    // }

    for (int i=0;i<m.size();i++){
        if( m.find("vaibhav") != m.end()  ){
            cout<<"found ";
            m.erase("vaibhav");
            break;
        }
        else{
            cout<<"not found : ";
        }
    }
    for(auto p:m){
        cout<<p.first<<' '<<p.second<<endl;
    }
}
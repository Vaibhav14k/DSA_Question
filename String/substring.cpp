    #include<iostream>
    using namespace std;
    int main(){
        string s = "vaibhav";
        int len=0;
        for(int st=0;st<=s.size();st++){
            for(int end=st+1;end<=s.size();end++){
                cout<<result;
                // len = max(len,result.length());
                if(result.length()>len){
                    len = result.length();
                }
                cout<<" ";
            }
            cout<<endl;
        }
        cout<<"maximum lenght : ;"<<len<<endl;
    }

#include<iostream>
#include<list>
using namespace std;
class mystack{
    list<int>ll;
    public:
        void push_back(int val){
            ll.push_front(val);
        }
        void pop_front(){
            ll.pop_front();
        }
        int top(){
            return ll.front();
        }
        bool empty(){
                return ll.size() ==0;
        }
};
int main(){
    //  Stack s;
    mystack s;
    s.push_back(10);
    s.push_back(20);
    s.push_back(30);
    while ( ! s.empty())
    {
        cout<<s.top()<<" ";  
        s.pop_front();  
    }
}
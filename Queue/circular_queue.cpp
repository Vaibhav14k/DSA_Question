#include<iostream>
using namespace std;

class Circularqueue{
    int* arr;
    int currsize,capacity;
    int f,r;
    public :
    Circularqueue(int n){
        currsize=0;
        capacity=n;
        f=0;
        r=-1;
        arr = new int[capacity];
    }
    void push(int val){
        if(currsize == capacity){
            cout<<"queue is full ";
        }else{
            r = (r + 1) % capacity;
            arr[r] = val;
            currsize++;
        }
    }
    void pop(){
        if( empty()){
            cout<<"queue is empty";
        }else{
            f = (f + 1) % capacity;
            currsize--;
        }
    }
    int top(){
        return arr[f];
    }
    bool empty(){
        return currsize == 0;
    }
    void print(){
        for(int i=0;i<capacity;i++){
            cout<< arr[i]<<" ";
        }
    }

};
int main(){
    Circularqueue cq(3);
    cq.push(1);
    cq.push(2);
    cq.push(3);
    cq.print();
}
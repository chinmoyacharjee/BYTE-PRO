#include<bits/stdc++.h>
using namespace std;
void performOprtion(long long int a,long long int b,long long int k,long long int *arr){
    for (int i=a-1;i<=b;i++){
        arr[i]+=k;
    }
}

int main(){
    long long int n,m;


    cin>>n>>m;
    long long int listArr[n];

    for(int i=0;i<n;i++){
        listArr[i]=0;
        //cout<<listArr[i]<<endl;
    }

    long long int a,b,k;
    for (int i=0;i<m;i++){
        cin>>a>>b>>k;
        performOprtion(a,b,k,listArr);
    }
    long long int maxValue = listArr[0];
    for(int i=1;i<n;i++){
        if(maxValue<=listArr[i]) maxValue=listArr[i];
    }

    for(int i=0;i<n;i++){
        //listArr[i]=0;
        cout<<listArr[i]<<endl;
    }
    cout<<maxValue<<endl;
    return 0;
}

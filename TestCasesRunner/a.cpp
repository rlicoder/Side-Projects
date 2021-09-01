#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    set<string> s;
    map<string,int> m;
    map<int,string> m1;
    vector<string> people;
    int c = 0;
    vector<vector<int>> adj(2001, vector<int>());
    vector<vector<int>> adjrev(2001, vector<int>());
    for (int i = 0; i < n; i++)
    {
        string name;
        cin >> name;
        people.push_back(name);
        if (!s.count(name))
        {
            m[name] = c++;
            m1[c-1] = name;
            s.insert(name);
        }
        string speak;
        cin >> speak;
        if (!s.count(speak))
        {
            m[speak] = c++;
            m1[c-1] = speak;
            s.insert(speak);
        }
        adj[m[name]].push_back(m[speak]);
        adj[m[speak]].push_back(m[name]);
        adjrev[m[speak]].push_back(m[name]);
        adjrev[m[name]].push_back(m[speak]);
        string str;
        getline(cin, str);
        stringstream ss(str);
        int count = 0;
        while (ss >> str)
        {
            count++;
            if (!s.count(str))
            {
                m[str] = c++;
                m1[c-1] = str;
                s.insert(str);
            }
            adj[m[str]].push_back(m[name]);
            adjrev[m[name]].push_back(m[str]);
        }
    }
    sort(people.begin(), people.end());
    //for (int i = 0; i < adj.size(); i++)
    //{
    //    if (adj[i].size() > 1)
    //    {
    //        for (int j = 0; j < adj[i].size(); j++)
    //        {
    //            cout << m1[i] << " speaks " << m1[adj[i][j]] << endl;
    //        }
    //    }
    //}

    
    vector<int> vis(2001, false);
    vector<int> visrev(2001, false);

    function<void(int)> dfs1 = [&] (int c)
    {
        vis[c] = true;
        //cout << "I have visitied" << m1[c] << endl;
        for (auto it : adj[c])
        {
            if (!vis[it])
            {
                dfs1(it);
            }
        }
    };
    
    function<void(int)> dfs2 = [&] (int c)
    {
        visrev[c] = true;
        for (auto it : adj[c])
        {
            if (!visrev[it])
            {
                dfs2(it);
            }
        }
    };

    int hi = 0;
    for (int i = 0; i < n; i++)
    {
        set<int> s;
        for (int j = 0; j < n; j++)
        {
            if (i == j) continue;
            vis.clear();
            visrev.clear();
            vis.resize(2001, false);
            visrev.resize(2001, false);
            int a, b;
            a = m[people[i]];
            b = m[people[j]];
            //cout << "dfs on " << m1[a] << "starting" << endl;
            dfs1(a);
            dfs2(b);
            if (vis[b] && visrev[a])
            {
                //cout << m1[a] << " can talk to  " << m1[b] << endl;
                s.insert(a);
                s.insert(b);
            }
        }
        hi = max(hi, (int)s.size());
    }
    cout << min(n - hi, n-1) << endl;
}

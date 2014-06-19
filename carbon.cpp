/*Paul A Glenn
 * carbon.cpp
 * Goal: to fill pdb file with c{alpha} carbons from iENM pdb.
 */
#include<iostream>
#include<fstream>
#include<string>
#include<cassert>
#include<cstdlib>
using namespace std;

ifstream& filecheck(int args, char* s[]) {
    if(args<2) {
        cerr<<"Usage: "<<s[0]<<"filename"<<endl;
        assert(args==3);
    }
    static ifstream the_file(s[1]);
    assert(the_file.is_open());
    return the_file;
}
int find(string str,string subString);

int main(int argc, char* argv[]) {
    ifstream& prev_file = filecheck(argc,argv); //Crystallography file
    ofstream outfile(argv[2]);
	string frame = "1";
    while(!prev_file.eof() ) {
        string line;
        getline(prev_file,line);
        if(find(line, "CA") && find(line, "FRAME"+frame+" ") )  {
            int ind1 = line.length()-10; //this is where the "frame" is 
            line.erase(ind1,string::npos); //we don't want it there. 
            line.insert(line.end(),5,' '); //instead insert the atom type
            line.push_back('C'); //refer to previous REQ
            outfile<<line<<endl;
        }   else  { }
    }
    outfile.close();
    return 0;

}

int find(string str,string subString) {
	return (str.find(subString) != string::npos);
}

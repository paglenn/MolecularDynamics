/*Paul A Glenn
 * fillpdb.cpp
 * Goal: to fill pdb file with c{alpha} carbons from iENM pdb.
 */
#include<iostream>
#include<fstream>
#include<string>
#include<cassert>
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

int main(int argc, char* argv[]) {
    ifstream& prev_file = filecheck(argc,argv); //Crystallography file
    ofstream outfile(argv[2]);

    while(!prev_file.eof() ) {
        string line;
        getline(prev_file,line);
        if(line.find("HOH")!=string::npos )  {
        }   else {
               outfile<<line<<endl; //allother file types written
        }
    }
    outfile.close();
    return 0;

}


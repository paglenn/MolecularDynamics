/*Paul A Glenn
 * fixpdb.cpp
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
        assert(args==4);
    }
    static ifstream the_file(s[1]);
    assert(the_file.is_open());
    return the_file;
}

int main(int argc, char* argv[]) {
    ifstream& prev_file = filecheck(argc,argv); //Crystallography file
    ifstream ca_file(argv[2]); //file from iENM
    ofstream outfile(argv[3]);

    while(!prev_file.eof() ) {
        string line;
        getline(prev_file,line);
        if(line.find("ATOM")!=string::npos && line.find("OH2")==string::npos && !ca_file.eof()  )  {
            string alt_line = "";
            getline(ca_file,alt_line);
            outfile<<alt_line<<endl;
        }   else {
               outfile<<line<<endl; //allother file types written
        }
    }
    outfile.close();
    return 0;

}


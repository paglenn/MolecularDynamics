/*Paul A Glenn
 * atomeq.cpp (Atom Equalizer)
 * Goal: Solvate target atom (from iENM) without help of VMD, 
 * so that #atoms equal for TMD
 * args: [a.out solvated_file dry_file output_file]
 */
#include<iostream>
#include<fstream>
#include<string>
#include<cassert>
#include<cstdlib>
using namespace std;


ifstream& filecheck(int args, char* s[]);
bool found(string str, string word); 

int main(int argc, char* argv[]) {
    ifstream& prev_file = filecheck(argc,argv);
    ifstream  incomplete_file(argv[2]);
    ofstream outfile(argv[3]); 
    size_t natoms = 19000; 
    if (argc==5) {natoms = atoi(argv[4]); }
    size_t itr = 0;
    while(!prev_file.eof() && itr <= natoms) {
        string line;
        getline(prev_file,line);
        
        if(found(line, "TIP")) {
            outfile<<line<<endl;
        } else {
            string alt_line; 
            getline(incomplete_file, alt_line);
            outfile<<alt_line<<endl;
        }
        ++itr; 
    }

    outfile.close();
    return 0;
}

bool found(string str, string word) { 
    return str.find(word)!=string::npos; 
    }

ifstream& filecheck(int args, char* s[]) {
    if(args<2) {
        cerr<<"Usage: "<<s[0]<<"filename"<<endl;
        assert(args==4);
    }
    static ifstream the_file(s[1]);
    assert(the_file.is_open());
    return the_file;
}


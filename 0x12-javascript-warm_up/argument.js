#!/usr/bin/node

const myVars =process.argv;
if (myVars.length === 2){
    console.log("No arguemant");
}
else if ( myVars.length === 3){
    console.log("Argument found");
}
else{
    console.log("Arguements found");
}

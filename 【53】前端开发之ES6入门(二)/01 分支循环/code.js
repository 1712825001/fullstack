for(let i=1;i<10;i++){
    line = '';
    for(let j=1;j<=i;j++){
        line += `${j}*${i}=${j*i}`;
    }
    console.log(line)
}

function hasPassingGrade(score) {
    if(score <= 59){
      return false
    }else{
      return true
    }
}


console.log(hasPassingGrade(100));
console.log(hasPassingGrade(53));
console.log(hasPassingGrade(87));
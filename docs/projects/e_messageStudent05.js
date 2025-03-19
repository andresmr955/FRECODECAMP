
function studentMsg(totalScores, studentScore) {
  var sScore = getGrade(studentScore)
  var aAverage = getAverage(totalScores)
  console.log(sScore, aAverage)
  if(hasPassingGrade(studentScore)){
    return "Class average: "+ aAverage +". Your grade: "+ sScore+". You passed the course."
  }else {
    return "Class average: "+ aAverage +". Your grade: "+ sScore+". You failed the course."
  }
}
console.log(studentMsg([92, 88, 12, 77, 57, 100, 67, 38, 97, 89], 37));
const colorList = [
  { hex: "#2C3E50", name: "Midnight Blue" },
  { hex: "#34495E", name: "Blue Gray" },
  { hex: "#2C2C2C", name: "Charcoal" },
  { hex: "#616A6B", name: "Steel Gray" },
  { hex: "#4A235A", name: "Deep Purple" },
  { hex: "#2F4F4F", name: "Dark Slate Gray" },
  { hex: "#0E4B5A", name: "Deep Teal" },
  { hex: "#36454F", name: "Charcoal Gray" },
  { hex: "#800020", name: "Burgundy" }
];
function getRandomIndex() {
  const randomIndex = Math.floor(colorList.length * Math.random());
  return randomIndex;
}

const body = document.querySelector("body");
const bgHexCodeSpanElement = document.querySelector("#bg-hex-code");

function changeBackgroundColor() {
  const color = colorList[getRandomIndex()]['hex'];
  const color_name = colorList[getRandomIndex()]['name']; 
  bgHexCodeSpanElement.innerText = color_name;
  body.style.backgroundColor = color;
}
const btn = document.querySelector("#btn");


btn.onclick = changeBackgroundColor;
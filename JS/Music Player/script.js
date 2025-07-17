const playlistSongs = document.getElementById('playlist-songs');
const playButton = document.getElementById("play");
const pauseButton = document.getElementById("pause");

const nextButton = document.getElementById('next');
const previousButton = document.getElementById('previous');
const shuffleButton = document.getElementById('shuffle');

let allSongs = [
    {
        id: 0,
        title: "Corazon Embustero",
        artist: "Carlos Munoz", 
        duration: "4:25", 
        src:"https://www.youtube.com/watch?v=afDEunyLpyw&list=RDafDEunyLpyw&start_radio=1&ab_channel=CafeRecords" 

    },
    {
    id: 1,
    title: "Scratching The Surface",
    artist: "Quincy Larson",
    duration: "4:25",
    src: "https://cdn.freecodecamp.org/curriculum/js-music-player/scratching-the-surface.mp3",
    },
    {
        id: 2,
title: "Still Learning",
artist: "Quincy Larson",
duration: "3:51",
src: "https://cdn.freecodecamp.org/curriculum/js-music-player/still-learning.mp3",
    }
];
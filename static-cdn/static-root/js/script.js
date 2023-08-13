// import FullyReveal from './FullyReveal.js';

window.onload = () => {
    // AOS.init();
    // var fullyReveal = new FullyReveal;
    // fullyReveal.init();

    let videocontainer = document.querySelector('.video-container video');
    let gallerycontainer = document.querySelector('.gallery-container img');
    let videolistcontainer = document.querySelector('.musicvideos-container .list-container');
    let gallerylistcontainer = document.querySelector('.photogallery-container .list-container');
    let videocontainerheight = videocontainer.getBoundingClientRect().height;
    let gallerycontainerheight = gallerycontainer.getBoundingClientRect().height;
    let backtotop = document.querySelectorAll('.backtotop');
    let gotomusic = document.querySelector('.go-to-music');
    let gotonextsection = document.querySelector('.go-to-next-section');
    let gotomusicvideo = document.querySelector('.go-to-musicvideo');
    let gotophotogallery = document.querySelector('.go-to-photogallery');
    let gotocontact = document.querySelector('.go-to-contact');
    let imagezoomincontainerimg = document.querySelector('.image-zoom-in-container img');
    let imagezoomincontainervideo = document.querySelector('.video-zoom-in-container video');
    let imagezoomout = document.querySelectorAll('.image-zoom-out');
    let videozoomout = document.querySelectorAll('.video-zoom-out');
    let opensharenav = document.querySelectorAll('.open-share-nav');
    let closesharenav = document.querySelectorAll('.close-share-nav');
    let aWrap = document.querySelectorAll('.aWrap');
    let playaudiotext = document.querySelectorAll('.play-audio-text');
    let customaudiocontrols = document.querySelectorAll('.custom-audio-controls');
    let sharethismusiccontainer = document.querySelectorAll('.share-this-music-container');
    let openmenu = document.querySelector('.open-menu');
    let closemenu = document.querySelector('.close-menu');
    let headermenuitemscontainer = document.querySelector('.header-menu-items-container');
    let closephonemenu = document.querySelector('.close-phone-menu');
    let phoneclickhandler = document.querySelectorAll('.phone-click-handler');
    let aPlayIco = document.querySelectorAll('.aPlay');
    let width = window.innerWidth;

    videolistcontainer.style.height = videocontainerheight + 'px';
    gallerylistcontainer.style.height = gallerycontainerheight + 'px';

    function currentYPosition() {
        // Firefox, Chrome, Opera, Safari
        if (self.pageYOffset) return self.pageYOffset;
        // Internet Explorer 6 - standards mode
        if (document.documentElement && document.documentElement.scrollTop)
            return document.documentElement.scrollTop;
        // Internet Explorer 6, 7 and 8
        if (document.body.scrollTop) return document.body.scrollTop;
        return 0;
    }

    function elmYPosition(eID) {
        var elm = document.getElementById(eID);
        var y = elm.offsetTop;
        var node = elm;
        while (node.offsetParent && node.offsetParent != document.body) {
            node = node.offsetParent;
            y += node.offsetTop;
        } return y;
    }

    function smoothScroll(eID) {
        var startY = currentYPosition();
        var stopY = elmYPosition(eID);
        var distance = stopY > startY ? stopY - startY : startY - stopY;
        if (distance < 100) {
            scrollTo(0, stopY); return;
        }
        var speed = Math.round(distance / 100);
        if (speed >= 20) speed = 20;
        var step = Math.round(distance / 25);
        var leapY = stopY > startY ? startY + step : startY - step;
        var timer = 0;
        if (stopY > startY) {
            for (var i = startY; i < stopY; i += step) {
                setTimeout('window.scrollTo(0, ' + leapY + ')', timer * speed);
                leapY += step; if (leapY > stopY) leapY = stopY; timer++;
            } return;
        }
        for (var i = startY; i > stopY; i -= step) {
            setTimeout('window.scrollTo(0, ' + leapY + ')', timer * speed);
            leapY -= step; if (leapY < stopY) leapY = stopY; timer++;
        }
        return false;
    }

    backtotop.forEach((element) => element.addEventListener('click', () => {
        smoothScroll('backtotop');
    }))

    gotomusic.addEventListener('click', () => {
        smoothScroll('music');
    })

    gotonextsection.addEventListener('click', () => {
        smoothScroll('music');
    })

    gotomusicvideo.addEventListener('click', () => {
        smoothScroll('musicvideo');
    })

    gotophotogallery.addEventListener('click', () => {
        smoothScroll('photogallery');
    })

    gotocontact.addEventListener('click', () => {
        smoothScroll('contact');
    })

    imagezoomout.forEach((element) => element.addEventListener('click', () => {
        let newimage = element.getAttribute('src');
        imagezoomincontainerimg.setAttribute('src', newimage);
    }))

    videozoomout.forEach((element) => element.addEventListener('click', () => {
        let newvideo = element.getAttribute('src');
        imagezoomincontainervideo.setAttribute('src', newvideo);
    }))

    window.addEventListener('click', () => {
        for (let i = 0; i < sharethismusiccontainer.length; i++) {
            sharethismusiccontainer[i].style.opacity = '0';
            sharethismusiccontainer[i].style.visibility = 'hidden';
        }

        for (let i = 0; i < aWrap.length; i++) {
            let textrealpos = ((i + 1) / 2) - 1;
            setTimeout(() => {
                if (playaudiotext[textrealpos]) {
                    playaudiotext[textrealpos].style.opacity = '1';
                    playaudiotext[textrealpos].style.visibility = 'visible';
                }

                aWrap[i].style.width = '125px';
                aWrap[i].classList.remove('no-hover');
            }, 500);

            customaudiocontrols[i].style.opacity = '0';
            customaudiocontrols[i].style.visibility = 'hidden';
        }
    })

    sharethismusiccontainer.forEach((element) => element.addEventListener('click', (e) => {
        e.stopPropagation();
    }))

    function closeall() {
        for (let i = 0; i < sharethismusiccontainer.length; i++) {
            sharethismusiccontainer[i].style.opacity = '0';
            sharethismusiccontainer[i].style.visibility = 'hidden';
        }

        for (let i = 0; i < aWrap.length; i++) {
            let textrealpos = ((i + 1) / 2) - 1;
            setTimeout(() => {
                if (playaudiotext[textrealpos]) {
                    playaudiotext[textrealpos].style.opacity = '1';
                    playaudiotext[textrealpos].style.visibility = 'visible';
                }

                aWrap[i].style.width = '125px';
                aWrap[i].classList.remove('no-hover');
            }, 500);

            customaudiocontrols[i].style.opacity = '0';
            customaudiocontrols[i].style.visibility = 'hidden';
        }
    }

    opensharenav.forEach((element, index) => element.addEventListener('click', (e) => {
        e.stopPropagation();

        closeall();

        sharethismusiccontainer[index].style.opacity = '1';
        sharethismusiccontainer[index].style.visibility = 'visible';
    }))

    closesharenav.forEach((element, index) => element.addEventListener('click', () => {
        sharethismusiccontainer[index].style.opacity = '0';
        sharethismusiccontainer[index].style.visibility = 'hidden';
    }))

    openmenu.addEventListener('click', () => {
        headermenuitemscontainer.style.opacity = '1';
        headermenuitemscontainer.style.visibility = 'visible';
        closephonemenu.style.opacity = '1';
        closephonemenu.style.visibility = 'visible';
    })

    closemenu.addEventListener('click', () => {
        headermenuitemscontainer.style.opacity = '0';
        headermenuitemscontainer.style.visibility = 'hidden';
        closephonemenu.style.opacity = '0';
        closephonemenu.style.visibility = 'hidden';
    })

    if (width <= 767) {
        phoneclickhandler.forEach((element) => element.addEventListener('click', () => {
            headermenuitemscontainer.style.opacity = '0';
            headermenuitemscontainer.style.visibility = 'hidden';
            closephonemenu.style.opacity = '0';
            closephonemenu.style.visibility = 'hidden';
        }))
    }

    // Custom Player Copyright 2023 - Coded by: https://mmzand.ir
    // Credit: https://code-boxx.com/html-custom-audio-player/#sec-audio
    aWrap.forEach((element, index) => element.addEventListener('click', (e) => {
        e.stopPropagation();

        if (width > 1199) {
            element.style.width = '550px';
            element.classList.add('no-hover');

            let textrealpos = ((index + 1) / 2) - 1;
            if (playaudiotext[textrealpos]) {
                playaudiotext[textrealpos].style.opacity = '0';
                playaudiotext[textrealpos].style.visibility = 'hidden';
            }

            customaudiocontrols[index].style.opacity = '1';
            customaudiocontrols[index].style.visibility = 'visible';
        }
    }))

    // (A) SUPPORT FUNCTION - FORMAT HH:MM:SS
    var timeString = secs => {
        // (A1) HOURS, MINUTES, SECONDS
        let ss = Math.floor(secs),
            hh = Math.floor(ss / 3600),
            mm = Math.floor((ss - (hh * 3600)) / 60);
        ss = ss - (hh * 3600) - (mm * 60);

        // (A2) RETURN FORMATTED TIME
        if (hh > 0) { mm = mm < 10 ? "0" + mm : mm; }
        ss = ss < 10 ? "0" + ss : ss;
        return hh > 0 ? `${hh}:${mm}:${ss}` : `${mm}:${ss}`;
    };

    function setProgress(elTarget) {
        let divisionNumber = elTarget.getAttribute('max') / 100;
        let rangeNewWidth = Math.floor(elTarget.value / divisionNumber);

        if (elTarget.value == 0) {
            elTarget.nextSibling.style.width = "0%";
            return;
        }

        if (rangeNewWidth > 95) {
            elTarget.nextSibling.style.width = rangeNewWidth + "%";
            elTarget.nextSibling.style.borderRadius = "10px";
        } else if (0 < rangeNewWidth < 11) {
            elTarget.nextSibling.style.width = rangeNewWidth + 1 + "%";
        } else {
            elTarget.nextSibling.style.width = rangeNewWidth + "%";
        }
    }

    for (let i of document.querySelectorAll(".aWrap")) {
        // (B) AUDIO + HTML SETUP + FLAGS
        i.audio = new Audio(encodeURI(i.dataset.src));
        i.aPlay = i.querySelector(".aPlay"),
            i.aPlayIco = i.querySelector(".aPlayIco"),
            i.aNow = i.querySelector(".aNow"),
            i.aTime = i.querySelector(".aTime"),
            i.aSeek = i.querySelector(".aSeek"),
            i.aVolume = i.querySelector(".aVolume"),
            i.aVolIco = i.querySelector(".aVolIco");
        i.seeking = false; // user is dragging the seek bar

        // (C) PLAY & PAUSE
        // (C1) CLICK TO PLAY/PAUSE
        i.aPlay.onclick = () => {
            if (i.audio.paused) { i.audio.play(); }
            else { i.audio.pause(); }
        };

        // (C2) SET PLAY/PAUSE ICON
        i.audio.onplay = () => i.aPlayIco.innerHTML = '<i class="fa fa-pause"></i>';
        i.audio.onpause = () => i.aPlayIco.innerHTML = '<i class="fa fa-play"></i>';

        // (D) TRACK PROGRESS & SEEK TIME
        // (D1) TRACK LOADING
        i.audio.onloadstart = () => {
            i.aNow.innerHTML = "Loading";
            i.aTime.innerHTML = "";
        };

        // (D2) ON META LOADED
        i.audio.onloadedmetadata = () => {
            // (D2-1) INIT SET TRACK TIME
            i.aNow.innerHTML = timeString(0);
            i.aTime.innerHTML = timeString(i.audio.duration);

            // (D2-2) SET SEEK BAR MAX TIME
            i.aSeek.max = Math.floor(i.audio.duration);

            // (D2-3) USER CHANGE SEEK BAR TIME
            i.aSeek.oninput = () => i.seeking = true; // prevents clash with (d2-4)
            i.aSeek.onchange = () => {
                i.audio.currentTime = i.aSeek.value;
                if (!i.audio.paused) { i.audio.play(); }
                i.seeking = false;
            };

            // (D2-4) UPDATE SEEK BAR ON PLAYING
            i.audio.ontimeupdate = () => {
                if (!i.seeking) { i.aSeek.value = Math.floor(i.audio.currentTime); }
                i.aNow.innerHTML = timeString(i.audio.currentTime);
                setProgress(i.aSeek);
            };
        };

        // (E) VOLUME
        i.aVolIco.onclick = () => {
            i.audio.volume = i.audio.volume == 0 ? 1 : 0;
            i.aVolume.value = i.audio.volume;
            i.aVolIco.innerHTML = (i.aVolume.value == 0 ? '<i class="fa fa-volume-off"></i>' : '<i class="fa fa-volume-up"></i>');
            setProgress(i.aVolume);
        };
        i.aVolume.onchange = () => {
            i.audio.volume = i.aVolume.value;
            i.aVolIco.innerHTML = (i.aVolume.value == 0 ? '<i class="fa fa-volume-off"></i>' : '<i class="fa fa-volume-up"></i>');
        };

        // (F) ENABLE/DISABLE CONTROLS
        i.audio.oncanplaythrough = () => {
            i.aPlay.disabled = false;
            i.aVolume.disabled = false;
            i.aSeek.disabled = false;
        };
        i.audio.onwaiting = () => {
            i.aPlay.disabled = true;
            i.aVolume.disabled = true;
            i.aSeek.disabled = true;
        };

        i.aSeek.addEventListener("input", function () {
            setProgress(this);
        });

        i.aVolume.addEventListener("input", function () {
            setProgress(this);
        });
    }

    // Custom Player Copyright 2023 - Coded by: https://FarzinShams.com

    console.log('Coded by: https://FarzinShams.com');
}

function isDescendant(parent, child) {
    return parent.contains(child);
}

const modal = document.getElementById("popup-modal");

document.getElementById("dokme").addEventListener("click", function () {
    modal.style.display = "none";
});

document.addEventListener("click", function (event) {
    const clickedElement = event.target;

    // Check if the clicked element is the modal or its descendant
    if (!isDescendant(modal, clickedElement)) {
        modal.style.display = "none";
    }
});

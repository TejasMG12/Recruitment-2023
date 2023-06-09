const fromText = document.querySelector(".from-text"),
    toText = document.querySelector(".to-text"),
    exchageIcon = document.querySelector(".exchange"),
    selectTag = document.querySelectorAll("select"),
    icons = document.querySelectorAll(".row i");
translateBtn = document.querySelector("button"),


    translateBtn.addEventListener("click", () => {

        let text = fromText.value.trim(),
            translateFrom = selectTag[0].value,
            translateTo = selectTag[1].value;
        if (!text) { return; }
        toText.setAttribute("placeholder", "Translating...");
        //toText.innerHTML="boom";
        // Todo: add api fetch from https://mymemory.translated.net/doc/spec.php
        fetch('https://api.mymemory.translated.net/get?q=' + text + '&langpair=' + translateFrom + '|' + translateTo)
            .then(response => response.json())
            .then(data => {
                toText.innerHTML = data.responseData.translatedText;

            })
    });
    document.getElementById("from2").addEventListener("click", function () {
        if (!fromText.value) return;
        // TODO: add code to copy to Clipboard for the icon with class fa-copy
        let text = fromText.value.trim();
        navigator.clipboard.writeText(text);

        // Alert the copied text
        alert("Copied the text: " + text);
    });
    document.getElementById("to2").addEventListener("click", function () {
       
        if ( !toText.value) return;
        // TODO: add code to copy to Clipboard for the icon with class fa-copy
        let text = toText.value.trim();
        navigator.clipboard.writeText(text);

        // Alert the copied text
        alert("Copied the text: " + text);
    });
    
    // TODO: add code for speechSynthesis for icon with classname fa-volume-up (text to speech)

    document.getElementById("from1").addEventListener("click", function () {
        if (!fromText.value) return;
        // TODO: add code to copy to Clipboard for the icon with class fa-copy
        let text = fromText.value.trim();
        
        
        let utterance = new SpeechSynthesisUtterance(text);
        speechSynthesis.speak(utterance);
        
        
    });
    document.getElementById("to1").addEventListener("click", function () {
        let text = toText.value.trim();
        if ( !toText.value) return;
        
        
        let utterance = new SpeechSynthesisUtterance(text);
        speechSynthesis.speak(utterance);
        
    });


document.getElementById("exc").addEventListener("click",() => {
    let //tempText = fromText.value,
       tempLang = selectTag[0].value;
       
   //fromText.value = toText.value;
   //toText.value = tempText;
   selectTag[0].value = selectTag[1].value;
   selectTag[1].value = tempLang;
});

selectTag.forEach((tag, id) => {
    for (let country_code in countries) {
        let selected = id == 0 ? country_code == "en-GB" ? "selected" : "" : country_code == "hi-IN" ? "selected" : "";
        let option = `<option ${selected} value="${country_code}">${countries[country_code]}</option>`;
        tag.insertAdjacentHTML("beforeend", option);
    }
});

fromText.addEventListener("keyup", () => {
    if (!fromText.value) {
        toText.value = "";
    }
});



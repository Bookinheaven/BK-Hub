document.addEventListener("visibilitychange", function () {
    if (!document.hidden) {
        showTauntMessage();
    }
});

let tauntActive = false;

function showTauntMessage() {
    if (tauntActive) return;
    tauntActive = true;

    const taunts = [
        "I am inevitable.",
        "Reality is often disappointing.",
        "You could not live with your own failure. And where did that bring you? Back to me.",
        "Dread it. Run from it. Destiny still arrives.",
        "I ignored my destiny once. I cannot do that again.",
        "The hardest choices require the strongest wills.",
        "Your efforts are nothing but dust in the wind.",
        "You’re not the only one cursed with knowledge.",
        "Fun isn’t something one considers when balancing the universe.",
        "You think you have power? I hold the fate of the universe in my grasp.",
        "You should’ve gone for the head.",
        "What did it cost? Everything.",
        "I could simply snap my fingers, and you would cease to exist.",
        "A small price to pay for salvation.",
        "The universe has judged you unworthy.",
        "Your persistence is amusing… yet pointless.",
        "I hope they remember you.",
        "You're merely delaying the inevitable.",
        "All that for a drop of blood?",
        "I will shred this universe down to its last atom.",
        "Stubborn, aren't you? Yet, ultimately futile.",
        "I am beyond your understanding.",
        "You're trying so hard… but for what?",
        "The universe doesn’t favor the weak.",
        "Your struggle is meaningless.",
        "You fight against fate itself.",
        "Everything must be perfectly balanced.",
        "I once had mercy… do not mistake that for weakness.",
        "No resurrections this time.",
        "The strong will always rule over the weak.",
        "This is the endgame.",
        "I have waited for this moment… and now, it is here.",
        "Even the most resilient will crumble before me.",
        "Your resistance only prolongs the suffering.",
        "I have won long before this battle began.",
        "You’re wasting time. Accept your fate.",
        "They called me a madman. They were wrong.",
        "I don't enjoy violence. But balance must be restored.",
        "You amuse me, but amusement is not victory.",
        "You are nothing but an ant before a god.",
        "Surrender. It is the logical conclusion.",
        "The more you resist, the more you suffer.",
        "This universe deserves correction, and I will see it done.",
        "You think you're strong? Strength is nothing without purpose.",
        "I will watch as your will crumbles into dust.",
        "Your struggle changes nothing.",
        "Even a Titan can feel pity… but not for long.",
        "Did you really think you had a chance?",
        "This battle is already over. You just don't know it yet.",
        "No one escapes their destiny.",
        "You think you are special? The universe does not care.",
        "Your efforts will be forgotten, but I will remain.",
        "You may delay me, but you will never stop me.",
        "The end is near.",
        "Your time is running out.",
        "This is the price of defying inevitability.",
        "You are unworthy of what you seek.",
        "You call this a challenge?",
        "Your arrogance blinds you.",
        "You are but a speck in my grand design.",
        "Everything leads to this moment.",
        "Do you feel it? The weight of failure pressing down on you?",
        "You stand before a god. Kneel.",
        "I have conquered countless worlds. You are nothing special.",
        "You cannot bargain with fate.",
        "You should have accepted your fate when you had the chance.",
        "Your defiance amuses me.",
        "Your fate was sealed long ago.",
        "This is where your story ends.",
        "Your journey leads only to dust.",
        "I offer you mercy. You should take it.",
        "Your resistance is but an echo of your fear.",
        "This universe belongs to me now.",
        "Your will is strong… but not strong enough.",
        "In the end, none of this will matter.",
        "Perhaps you believe in hope. That is your mistake.",
        "Even the mightiest fall before me.",
        "It’s time you accepted your place in the universe.",
        "I do not hate you. You simply do not matter.",
        "Your suffering is inevitable.",
        "You had your chance. You failed.",
        "Everything you’ve built will be gone in an instant.",
        "You delay the unavoidable. But only for so long.",
        "This is balance. This is order.",
        "It’s over before it even began.",
        "The universe bends to my will. You are no exception.",
        "I admire your determination. But it changes nothing.",
        "You fight for nothing. I fight for everything.",
        "Your hope is a disease. And I am the cure.",
        "You will be remembered… as nothing but dust.",
        "The end has already been written.",
        "You are unprepared for what comes next.",
        "Accept it. Your time is up.",
        "What is inevitable… cannot be denied.",
        "Dust… is all that will remain."
    ];

    const randomTaunt = taunts[Math.floor(Math.random() * taunts.length)];
    
    let tauntBox = document.createElement("div");
    tauntBox.classList.add("taunt-box");
    tauntBox.innerText = randomTaunt;
    
    document.body.appendChild(tauntBox);
    
    setTimeout(() => {
        tauntBox.classList.add("fade-out");
        tauntActive = false;
        setTimeout(() => {
            tauntBox.remove();
        }, 6000);
    }, 6000);
}

function downloadPCAP() {
    console.log('ads')

    const fileUrl = "thanos_data.pcap";  
    const a = document.createElement("a");
    a.href = fileUrl;
    a.download = "thanos_data.pcap";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

document.addEventListener("DOMContentLoaded", function () {
    const downloadBtn = document.getElementById("download-btn");
    if (downloadBtn) {
        downloadBtn.addEventListener("click", downloadPCAP);
    }
});

alert("Rawr *suspenceful music*")
console.log("huhuhu")

const form = document.querySelector("#task-form")
const input = document.querySelector("#task-inout")
const list = document.querySelector("#task-list")

let Schedule = [];
function saveSchedule() {
    localStorage.setItem("Schedule", JSON.stringify(Schedule));
}

function saveSchedule(Schedule){
    if (Schedule === "") return;
    const text = { id: crypto.randomUUID(), Schedule:text, done: false
    };
    Schedule.push(Schedule);
    saveSchedule();
    renderSchedule();
}

function renderSchedule() {
    list.innerHTML =""

    Schedule.forEach((Schedule) => {
        const li = document.createElement("li")

        const text = document.createElement("spam")
        text.textContent = Schedule.text
        if (Schedule.done){
            text.style.textDecoration = "line-through"
        }
        const doneBtn = document.createElement("button")
        doneBtn.textContent = Schedule.done ?
        "undo": "done"
        doneBtn.addEventListener("click ",() => {
            toggleSchedule(Schedule.id)
            console.log("test")
        })
        const deleteBtn = document.createElement("button")
        deleteBtn.textContent ="delete"
        deleteBtn.addEventListener("click", ()=>{
            toggleSchedule(Schedule.id)
            console.log("hest")

        })

        li.appendChild(text)
        li.appendChild(doneBtn)
        li.appendChild(deleteBtn)
        list.appendChild(li)

    })
    
}
function toggleSchedule(id) {
    const Schedule = Schedule.find(t => t.id === id)
    if (!Schedule) return Schedule.done= !Schedule.done
    saveSchedule()
    renderSchedule()
}

function toggleSchedule(id) {
    Schedule = Schedule.filter(t => t.id !== id)
    saveSchedule()
    renderSchedule()
}
form.addEventListener("submit", (e) =>{
    e.preventDefault()
    const text = input.value.trim()    
    saveSchedule(text)
    input.value = ""

})

renderSchedule()
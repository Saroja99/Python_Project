const questions = [
    {
        question: "What is the capital of France?",
        options: ["Madrid", "Rome", "Paris", "Berlin"],
        answer: "Paris",
        wire: "red"
    },
    {
        question: "What is 5 + 7?",
        options: ["10", "12", "13", "14"],
        answer: "12",
        wire: "blue"
    },
    {
        question: "Who wrote 'To Kill a Mockingbird'?",
        options: ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"],
        answer: "Harper Lee",
        wire: "green"
    },
    {
        question: "What is the largest planet in our solar system?",
        options: ["Earth", "Mars", "Jupiter", "Saturn"],
        answer: "Jupiter",
        wire: "yellow"
    },
    {
        question: "Which element has the chemical symbol 'O'?",
        options: ["Gold", "Oxygen", "Silver", "Helium"],
        answer: "Oxygen",
        wire: "black"
    }
];

let currentQuestion = 0;
let correctWires = [];

document.addEventListener('DOMContentLoaded', () => {
    loadQuestion();
});

function loadQuestion() {
    if (currentQuestion < questions.length) {
        const questionData = questions[currentQuestion];
        document.getElementById('question').innerText = questionData.question;

        const optionsDiv = document.getElementById('options');
        optionsDiv.innerHTML = '';
        questionData.options.forEach(option => {
            const label = document.createElement('label');
            label.classList.add('option');
            const input = document.createElement('input');
            input.type = 'radio';
            input.name = 'option';
            input.value = option;
            label.appendChild(input);
            label.appendChild(document.createTextNode(option));
            optionsDiv.appendChild(label);
        });
    }
}

function checkAnswer() {
    const selectedOption = document.querySelector('input[name="option"]:checked');
    if (selectedOption) {
        const answer = selectedOption.value;
        const correctAnswer = questions[currentQuestion].answer;

        if (answer === correctAnswer) {
            correctWires.push(questions[currentQuestion].wire);
            currentQuestion++;
            if (currentQuestion < questions.length) {
                loadQuestion();
            } else {
                diffuseBomb();
            }
        } else {
            explodeBomb();
        }
    } else {
        alert('Please select an option.');
    }
}

function diffuseBomb() {
    document.getElementById('quiz').style.display = 'none';
    document.getElementById('result').innerText = "Congratulations! You have successfully diffused the bomb.";
    document.getElementById('result').style.color = 'green';
}

function explodeBomb() {
    document.getElementById('quiz').style.display = 'none';
    document.getElementById('result').innerText = "Boom! You cut the wrong wire and the bomb exploded.";
}

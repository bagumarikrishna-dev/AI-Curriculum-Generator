function generateCurriculum() {
    let topic = document.getElementById("topic").value;

    let curriculum = `
        <h3>Curriculum for ${topic}</h3>
        <ul>
            <li>Module 1: Introduction</li>
            <li>Module 2: Basics</li>
            <li>Module 3: Intermediate Concepts</li>
            <li>Module 4: Advanced Concepts</li>
            <li>Module 5: Projects</li>
        </ul>
    `;

    document.getElementById("result").innerHTML = curriculum;
}
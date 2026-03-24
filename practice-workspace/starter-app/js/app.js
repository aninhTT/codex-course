const dashboardData = {
  priorities: [
    "Turn meeting notes into a polished weekly recap",
    "Track follow-ups from the operations sync",
    "Draft a simple dashboard for recurring work"
  ],
  wins: [
    "Consolidated scattered updates into one place",
    "Reduced time spent rewriting summaries"
  ],
  followups: [
    "Choose a weekly recap format the team will reuse",
    "List 3 workflow ideas Codex could help with",
    "Personalize this dashboard around one real task"
  ]
};

function renderList(elementId, items) {
  const list = document.getElementById(elementId);
  items.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    list.appendChild(li);
  });
}

renderList("priorities", dashboardData.priorities);
renderList("wins", dashboardData.wins);
renderList("followups", dashboardData.followups);

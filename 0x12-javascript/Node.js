const express = require('express');
const app = express();
const port = 3000;

// Middleware
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

// Routes
app.get('/', (req, res) => {
  res.send('Welcome to the To-Do List App!');
});

app.get('/tasks', (req, res) => {
  // Logic to fetch tasks from the database
  const tasks = [];

  res.json(tasks);
});

app.post('/tasks', (req, res) => {
  // Logic to create a new task in the database
  const { taskName } = req.body;

  // Code to create the task

  res.send('Task created successfully');
});

app.put('/tasks/:id', (req, res) => {
  const taskId = req.params.id;
  // Logic to update a task in the database

  res.send(`Task with ID ${taskId} updated successfully`);
});

app.delete('/tasks/:id', (req, res) => {
  const taskId = req.params.id;
  // Logic to delete a task from the database

  res.send(`Task with ID ${taskId} deleted successfully`);
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

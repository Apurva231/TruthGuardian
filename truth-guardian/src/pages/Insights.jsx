import React from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  LineElement,
  PointElement,
  Tooltip,
  Legend,
} from 'chart.js';
import './Insights.css'; // You can create this for extra styling

ChartJS.register(
  CategoryScale,
  LinearScale,
  LineElement,
  PointElement,
  Tooltip,
  Legend
);

const Insights = () => {
  const fakeData = {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    datasets: [
      {
        label: 'Fake News Reports',
        data: [12, 19, 3, 17, 28, 24, 20],
        fill: true,
        borderColor: '#0FA4AF',
        backgroundColor: 'rgba(15, 164, 175, 0.2)',
        tension: 0.4,
        pointRadius: 5,
        pointHoverRadius: 7,
      },
    ],
  };

  const fakeOptions = {
    responsive: true,
    plugins: {
      legend: {
        labels: {
          color: '#AFDDE5',
        },
      },
      tooltip: {
        backgroundColor: '#024950',
        titleColor: '#AFDDE5',
        bodyColor: '#AFDDE5',
      },
    },
    scales: {
      x: {
        ticks: { color: '#AFDDE5' },
        grid: { color: 'rgba(175, 221, 229, 0.1)' },
      },
      y: {
        ticks: { color: '#AFDDE5' },
        grid: { color: 'rgba(175, 221, 229, 0.1)' },
      },
    },
  };

  const insights = [
    '🖼 Image-based misinformation was the most reported this week.',
    '📈 Sharp rise in fake news around trending events mid-week.',
    '🔊 Audio deepfakes continue growing in volume & complexity.',
    '✅ Detection accuracy remains above 90% across all modules.',
  ];

  return (
    <div className="insights-container">
      <header className="insights-header">
        <h1>📊 Analytics & Insights</h1>
        <p>
          Uncover patterns in misinformation trends and how Truth Guardian tackles them.
        </p>
      </header>

      <div className="chart-section">
        <Line data={fakeData} options={fakeOptions} />
      </div>

      <section className="insight-summary">
        <h2>💡 Key Highlights This Week</h2>
        <div className="insight-cards">
          {insights.map((item, idx) => (
            <div className="card" key={idx}>
              <p>{item}</p>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};

export default Insights;
"use client";

import { motion } from "framer-motion";
import { ExternalLink, Activity } from "lucide-react";
import { FaGithub } from "react-icons/fa";

const projects = [
  {
    title: "Phishing URL Detection",
    description: "A machine learning system that detects whether a URL is phishing or legitimate using URL-based features.",
    problem: "Identifying malicious links before users click them by analyzing structural URL attributes.",
    tech: ["Python", "Pandas", "Scikit-learn", "Random Forest"],
    metrics: [
      { label: "Accuracy", value: "99.80%" },
      { label: "Precision", value: "99.70%" },
      { label: "Recall", value: "99.95%" },
      { label: "F1 Score", value: "99.82%" },
    ],
    github: "https://github.com",
    demo: null,
    gradient: "from-blue-600/20 to-cyan-600/20"
  },
  {
    title: "Computer Vision Image Classification",
    description: "Deep learning model utilizing transfer learning to accurately classify images across distinct categories.",
    problem: "Building a highly accurate image classifier without training massive models from scratch.",
    tech: ["TensorFlow", "Keras", "CNN", "Transfer Learning"],
    metrics: [
      { label: "Validation Acc", value: "High" },
      { label: "Loss", value: "Minimized" },
    ],
    github: "https://github.com",
    demo: null,
    gradient: "from-purple-600/20 to-pink-600/20"
  },
  {
    title: "Home Loan Default Prediction",
    description: "Predictive model to analyze customer data and determine loan default eligibility.",
    problem: "Assessing financial risk efficiently to automate loan approval processes.",
    tech: ["Python", "Pandas", "Scikit-learn", "Machine Learning"],
    metrics: [
      { label: "Predictive Power", value: "Robust" },
      { label: "Feature Impt", value: "Extracted" },
    ],
    github: "https://github.com",
    demo: null,
    gradient: "from-emerald-600/20 to-teal-600/20"
  },
  {
    title: "Generative AI / RAG Pipeline",
    description: "Advanced Retrieval-Augmented Generation system for document Q&A.",
    problem: "Answering complex queries reliably based on custom context.",
    tech: ["LLMs", "LangChain", "Vector DB", "Transformers"],
    metrics: [],
    github: null,
    demo: null,
    comingSoon: true,
    gradient: "from-orange-600/20 to-red-600/20"
  }
];

export default function Projects() {
  return (
    <section id="projects" className="py-24 relative">
      <div className="container mx-auto px-6 md:px-12">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12 flex flex-col md:flex-row md:items-end justify-between gap-4"
        >
          <div>
            <h2 className="text-3xl md:text-4xl font-bold mb-4">Featured Projects</h2>
            <div className="w-20 h-1 bg-blue-600 rounded-full mb-4"></div>
            <p className="text-gray-400 max-w-2xl text-lg">Practical applications of AI/ML showcasing end-to-end development, from data processing to model evaluation.</p>
          </div>
        </motion.div>

        <div className="grid md:grid-cols-2 gap-8">
          {projects.map((project, idx) => (
            <motion.div
              key={idx}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: idx * 0.1 }}
              className={`glass rounded-2xl overflow-hidden group hover:border-blue-500/30 transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_10px_30px_rgba(59,130,246,0.1)] relative`}
            >
              {/* Background abstract gradient */}
              <div className={`absolute inset-0 bg-gradient-to-br ${project.gradient} opacity-0 group-hover:opacity-100 transition-opacity duration-500`}></div>
              
              <div className="p-8 relative z-10 flex flex-col h-full">
                {project.comingSoon && (
                  <span className="absolute top-6 right-6 px-3 py-1 bg-white/10 rounded-full text-xs font-semibold text-white uppercase tracking-wider backdrop-blur-md border border-white/10">
                    Coming Soon
                  </span>
                )}
                
                <h3 className="text-2xl font-bold text-white mb-3 group-hover:text-blue-400 transition-colors">{project.title}</h3>
                <p className="text-gray-400 mb-4">{project.description}</p>
                
                <div className="mb-6">
                  <p className="text-sm text-gray-500 font-medium mb-1 uppercase tracking-wider">Problem Solved</p>
                  <p className="text-gray-300 text-sm">{project.problem}</p>
                </div>

                {/* Metrics */}
                {project.metrics.length > 0 && (
                  <div className="mb-6 bg-black/30 rounded-xl p-4 border border-white/5">
                    <div className="flex items-center gap-2 mb-3 text-sm font-medium text-gray-400">
                      <Activity size={16} /> Key Metrics
                    </div>
                    <div className="grid grid-cols-2 gap-3">
                      {project.metrics.map((metric, mIdx) => (
                        <div key={mIdx}>
                          <p className="text-xs text-gray-500">{metric.label}</p>
                          <p className="text-white font-mono font-semibold">{metric.value}</p>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                <div className="mt-auto pt-6 flex flex-wrap items-center justify-between gap-4 border-t border-white/10">
                  <div className="flex flex-wrap gap-2">
                    {project.tech.map((t, tIdx) => (
                      <span key={tIdx} className="text-xs font-medium text-blue-300 bg-blue-500/10 px-2 py-1 rounded">
                        {t}
                      </span>
                    ))}
                  </div>
                  
                  <div className="flex items-center gap-3">
                    {project.github && (
                      <a href={project.github} target="_blank" rel="noreferrer" className="p-2 rounded-full bg-white/5 hover:bg-white/20 text-white transition-colors">
                        <FaGithub size={20} />
                      </a>
                    )}
                    {project.demo && (
                      <a href={project.demo} target="_blank" rel="noreferrer" className="p-2 rounded-full bg-blue-600 hover:bg-blue-500 text-white transition-colors">
                        <ExternalLink size={20} />
                      </a>
                    )}
                  </div>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}

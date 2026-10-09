"use client";

import { motion } from "framer-motion";
import { Brain, Cpu, Sparkles, Rocket } from "lucide-react";

const skillCategories = [
  {
    title: "Machine Learning",
    icon: Brain,
    color: "text-blue-400",
    bgColor: "bg-blue-400/10",
    skills: ["Python", "NumPy", "Pandas", "Scikit-learn", "Matplotlib", "Seaborn", "Feature Engineering", "Model Evaluation"]
  },
  {
    title: "Deep Learning",
    icon: Cpu,
    color: "text-purple-400",
    bgColor: "bg-purple-400/10",
    skills: ["TensorFlow", "Keras", "Neural Networks", "CNN", "Transfer Learning", "Computer Vision"]
  },
  {
    title: "Generative AI",
    icon: Sparkles,
    color: "text-emerald-400",
    bgColor: "bg-emerald-400/10",
    skills: ["LLMs", "Prompt Engineering", "RAG", "Transformers", "LangChain"]
  },
  {
    title: "Development & Deployment",
    icon: Rocket,
    color: "text-orange-400",
    bgColor: "bg-orange-400/10",
    skills: ["Git", "GitHub", "Streamlit", "Flask/FastAPI", "REST APIs", "Docker", "Vercel"]
  }
];

export default function Skills() {
  return (
    <section id="skills" className="py-24 relative bg-black/20">
      <div className="container mx-auto px-6 md:px-12">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12"
        >
          <h2 className="text-3xl md:text-4xl font-bold mb-4">Technical Skills</h2>
          <div className="w-20 h-1 bg-blue-600 rounded-full"></div>
        </motion.div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {skillCategories.map((category, idx) => (
            <motion.div
              key={idx}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: idx * 0.1 }}
              className="glass p-6 rounded-2xl hover:-translate-y-2 transition-transform duration-300"
            >
              <div className={`w-12 h-12 rounded-xl flex items-center justify-center mb-6 ${category.bgColor} ${category.color}`}>
                <category.icon size={24} />
              </div>
              <h3 className="text-xl font-bold text-white mb-4">{category.title}</h3>
              <div className="flex flex-wrap gap-2">
                {category.skills.map((skill, sIdx) => (
                  <span 
                    key={sIdx}
                    className="px-3 py-1 bg-white/5 border border-white/10 rounded-full text-sm text-gray-300 font-medium"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}

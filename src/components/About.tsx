"use client";

import { motion } from "framer-motion";
import { GraduationCap, BrainCircuit, Code, Braces } from "lucide-react";

export default function About() {
  const stats = [
    { icon: GraduationCap, label: "BCA Graduate", desc: "Computer Science" },
    { icon: BrainCircuit, label: "AI/ML Focused", desc: "Core Specialization" },
    { icon: Code, label: "Python Developer", desc: "Primary Ecosystem" },
    { icon: Braces, label: "Project-Based Learning", desc: "Hands-on Experience" },
  ];

  return (
    <section id="about" className="py-24 relative">
      <div className="container mx-auto px-6 md:px-12">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12"
        >
          <h2 className="text-3xl md:text-4xl font-bold mb-4">About Me</h2>
          <div className="w-20 h-1 bg-blue-600 rounded-full"></div>
        </motion.div>

        <div className="grid lg:grid-cols-2 gap-12 items-center">
          <motion.div 
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="space-y-6 text-gray-300 text-lg"
          >
            <p>
              I am a BCA graduate highly focused on <strong className="text-white">Artificial Intelligence and Machine Learning</strong>. My passion lies in understanding how data can be transformed into intelligent, predictive solutions.
            </p>
            <p>
              My hands-on learning journey spans across <strong className="text-blue-400">Machine Learning, Deep Learning, Computer Vision, Data Science, and Generative AI</strong>. I believe in learning by doing, which is why my focus is heavily oriented towards practical project development—from initial data exploration and model building, all the way to evaluation and deployment.
            </p>
            <p>
              As an entry-level engineer, I am eager to apply my technical foundations in real-world scenarios, contribute to impactful AI products, and continuously grow my expertise in modern AI stacks.
            </p>
          </motion.div>

          <motion.div 
            initial={{ opacity: 0, x: 30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="grid grid-cols-2 gap-4"
          >
            {stats.map((stat, idx) => (
              <div key={idx} className="glass p-6 rounded-2xl flex flex-col items-center text-center gap-3 hover:border-blue-500/50 transition-colors">
                <div className="w-12 h-12 rounded-full bg-blue-500/10 flex items-center justify-center text-blue-400">
                  <stat.icon size={24} />
                </div>
                <div>
                  <h3 className="text-white font-semibold">{stat.label}</h3>
                  <p className="text-sm text-gray-400">{stat.desc}</p>
                </div>
              </div>
            ))}
          </motion.div>
        </div>
      </div>
    </section>
  );
}

"use client";

import { motion } from "framer-motion";
import { BookOpen, ChevronDown } from "lucide-react";

export default function Education() {
  const journey = [
    "Data Science",
    "Machine Learning",
    "Deep Learning",
    "Computer Vision",
    "Generative AI"
  ];

  return (
    <section id="education" className="py-24 relative bg-black/20">
      <div className="container mx-auto px-6 md:px-12">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12 flex flex-col items-center text-center"
        >
          <h2 className="text-3xl md:text-4xl font-bold mb-4">Education & Learning Journey</h2>
          <div className="w-20 h-1 bg-blue-600 rounded-full mb-8"></div>
        </motion.div>

        <div className="grid md:grid-cols-2 gap-12 items-start max-w-5xl mx-auto">
          {/* Formal Education */}
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="glass p-8 rounded-2xl relative overflow-hidden"
          >
            <div className="absolute top-0 right-0 w-32 h-32 bg-blue-500/10 rounded-bl-full"></div>
            
            <div className="flex items-center gap-4 mb-6 relative z-10">
              <div className="w-12 h-12 bg-blue-600 rounded-xl flex items-center justify-center text-white shadow-lg shadow-blue-600/30">
                <BookOpen size={24} />
              </div>
              <div>
                <h3 className="text-2xl font-bold text-white">Bachelor of Computer Applications</h3>
                <p className="text-blue-400 font-medium">BCA Graduate</p>
              </div>
            </div>
            
            <p className="text-gray-400 leading-relaxed relative z-10">
              Completed foundational education in computer science, software engineering, and database management, providing a strong structural backing for complex AI/ML algorithms and production deployments.
            </p>
          </motion.div>

          {/* Learning Progression */}
          <motion.div
            initial={{ opacity: 0, x: 30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="flex flex-col gap-4"
          >
            <h3 className="text-xl font-semibold text-white mb-2 px-2">Technical Progression</h3>
            
            {journey.map((step, idx) => (
              <div key={idx} className="flex flex-col">
                <motion.div 
                  initial={{ opacity: 0, y: 10 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: idx * 0.15 }}
                  className="glass p-4 rounded-xl border border-white/5 flex items-center justify-between group hover:border-blue-500/30 transition-colors"
                >
                  <span className="text-gray-300 font-medium group-hover:text-white transition-colors">{step}</span>
                  <div className="w-8 h-8 rounded-full bg-white/5 flex items-center justify-center text-blue-400 font-mono text-xs">
                    0{idx + 1}
                  </div>
                </motion.div>
                {idx < journey.length - 1 && (
                  <div className="h-6 w-full flex justify-center py-1">
                    <ChevronDown size={16} className="text-gray-600" />
                  </div>
                )}
              </div>
            ))}
          </motion.div>
        </div>
      </div>
    </section>
  );
}

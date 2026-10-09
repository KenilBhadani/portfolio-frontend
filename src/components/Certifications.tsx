"use client";

import { motion } from "framer-motion";
import { Award, ExternalLink } from "lucide-react";

export default function Certifications() {
  const certifications = [
    {
      title: "Certified AI & ML Specialist",
      org: "DataMites",
      year: "Completed",
      link: "#"
    }
  ];

  return (
    <section id="certifications" className="py-24 relative">
      <div className="container mx-auto px-6 md:px-12 max-w-5xl">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12"
        >
          <h2 className="text-3xl md:text-4xl font-bold mb-4">Certifications</h2>
          <div className="w-20 h-1 bg-blue-600 rounded-full"></div>
        </motion.div>

        <div className="grid md:grid-cols-2 gap-6">
          {certifications.map((cert, idx) => (
            <motion.div
              key={idx}
              initial={{ opacity: 0, scale: 0.95 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              className="glass p-6 rounded-2xl border-l-4 border-l-blue-500 flex items-start gap-4 hover:bg-white/5 transition-colors"
            >
              <div className="w-10 h-10 rounded-full bg-blue-500/20 flex items-center justify-center text-blue-400 shrink-0 mt-1">
                <Award size={20} />
              </div>
              <div className="flex-1">
                <h3 className="text-lg font-bold text-white mb-1">{cert.title}</h3>
                <p className="text-blue-300 text-sm font-medium mb-2">{cert.org}</p>
                <div className="flex items-center justify-between mt-4 pt-4 border-t border-white/10">
                  <span className="text-gray-400 text-sm">{cert.year}</span>
                  {cert.link !== "#" && (
                    <a href={cert.link} className="text-gray-400 hover:text-white flex items-center gap-1 text-sm transition-colors">
                      Credential <ExternalLink size={14} />
                    </a>
                  )}
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}

import unittest
import subprocess
import os
import glob

class TestJavaCompilation(unittest.TestCase):
    
    def test_javac_compilation_integrity(self):
        # We test all Java files in the src directory to ensure they compile correctly
        # This guarantees zero syntax errors and that standard libraries are correctly imported.
        src_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src")
        java_files = glob.glob(os.path.join(src_dir, "*.java"))
        
        self.assertTrue(len(java_files) > 0, "No Java files found to compile.")
        
        for file in java_files:
            # Execute the Java Compiler
            result = subprocess.run(["javac", file], capture_output=True, text=True)
            self.assertEqual(
                result.returncode, 
                0, 
                msg=f"Java compilation failed for {os.path.basename(file)}:\n{result.stderr}"
            )
            
            # Clean up the generated .class files after compilation
            class_file = file.replace(".java", ".class")
            if os.path.exists(class_file):
                os.remove(class_file)

if __name__ == '__main__':
    unittest.main()

# pip install PyQt5
import sys 
import os 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QDesktopWidget, QFileDialog, QLineEdit, QLabel  
from PyQt5.QtCore import Qt
import subprocess

class NewWindow(QWidget):  
    def __init__(self, title, main_window):  
        super().__init__()  
        self.main_window = main_window  
        self.file_path = None
        self.file_path1 = None  
        self.index_dir = None  
        self.setWindowTitle(title)  
        self.setStyleSheet("background-color: #66CDAA;")  
        self.resize(850, 550)  
        self.center()  # Центрируем окно 
 
        layout = QVBoxLayout()  
        self.status_label = QLabel()

        if self.windowTitle() in ["сборка генома", "картирование", "сборка и аннотация (конвейер)", "SNP и индели"]:
            self.file_edit1 = QLineEdit(self)  
            self.file_edit1.setPlaceholderText("Выберите файл...")  
            self.file_edit1.setFixedSize(600, 100)  
            layout.addWidget(self.file_edit1, alignment=Qt.AlignCenter)

        self.file_edit = QLineEdit(self)  
        self.file_edit.setPlaceholderText("Выберите файл...")  
        self.file_edit.setFixedSize(600, 100)  
        layout.addWidget(self.file_edit, alignment=Qt.AlignCenter)  

        if self.windowTitle() == "сборка генома":
            self.status_label = QLabel(self) 
            self.status_label.setFixedSize(600, 100)
            self.status_label.setText("На вход принимаются 2 файла в формате fastq")
            layout.addWidget(self.status_label, alignment=Qt.AlignCenter)
            self.file_button1 = QPushButton("Выбрать файл", self)  
            self.file_button1.clicked.connect(self.open_file_dialog1)
            self.file_button1.setFixedSize(600, 100)  
            self.file_button1.setStyleSheet("background-color: #4CAF50; color: white;")
            layout.addWidget(self.file_button1, alignment=Qt.AlignCenter)
             
        
        if self.windowTitle() == "индексация": 
            self.status_label = QLabel(self)
            self.status_label.setFixedSize(600, 100)
            self.status_label.setText("На вход принимается файл в формате fasta")
            layout.addWidget(self.status_label, alignment=Qt.AlignCenter)   

        if self.windowTitle() == "картирование":
            self.status_label = QLabel(self)
            self.status_label.setFixedSize(600, 100)
            self.status_label.setWordWrap(True)
            self.status_label.setText("На вход принимаются 2 файла: 1 - файл референса (fasta) 2 - файл выравнивания (fastq)")
            layout.addWidget(self.status_label, alignment=Qt.AlignCenter)   
            self.file_button1 = QPushButton("Выбрать файл", self)  
            self.file_button1.clicked.connect(self.open_file_dialog1)
            self.file_button1.setFixedSize(600, 100)  
            self.file_button1.setStyleSheet("background-color: #4CAF50; color: white;")
            layout.addWidget(self.file_button1, alignment=Qt.AlignCenter) 

        if self.windowTitle() == "SNP и индели":
            self.status_label = QLabel(self)
            self.status_label.setFixedSize(600, 100)
            self.status_label.setWordWrap(True)
            self.status_label.setText("На вход принимаются 2 файла: 1 - файл референса (fasta) 2 - файл выравнивания (bam)")  
            layout.addWidget(self.status_label, alignment=Qt.AlignCenter)
            self.file_button1 = QPushButton("Выбрать файл", self)  
            self.file_button1.clicked.connect(self.open_file_dialog1)
            self.file_button1.setFixedSize(600, 100)  
            self.file_button1.setStyleSheet("background-color: #4CAF50; color: white;")
            layout.addWidget(self.file_button1, alignment=Qt.AlignCenter) 

        if self.windowTitle() == "сборка и аннотация (конвейер)":
            self.status_label = QLabel(self) 
            self.status_label.setFixedSize(600, 100)
            self.status_label.setText("На вход принимаются 2 файла в формате fastq")  
            layout.addWidget(self.status_label, alignment=Qt.AlignCenter)
            self.file_button1 = QPushButton("Выбрать файл", self)  
            self.file_button1.clicked.connect(self.open_file_dialog1)
            self.file_button1.setFixedSize(600, 100)  
            self.file_button1.setStyleSheet("background-color: #4CAF50; color: white;")
            layout.addWidget(self.file_button1, alignment=Qt.AlignCenter) 

        file_button = QPushButton("Выбрать файл", self)  
        file_button.clicked.connect(self.open_file_dialog)  

        start_button = QPushButton("Старт", self)  
        start_button.clicked.connect(self.start)  

        back_button = QPushButton("Назад", self)  
        back_button.clicked.connect(self.close_window)  

        # Установка размера и стиля кнопок  
        for btn in (file_button, start_button, back_button):  
            btn.setFixedSize(600, 100)  
            btn.setStyleSheet("background-color: #4CAF50; color: white;")  

        # Создание вертикального лэйаута для центрирования кнопок  
        btn_layout = QVBoxLayout()  
        btn_layout.addWidget(file_button)  
        btn_layout.addWidget(start_button)  
        btn_layout.addWidget(back_button)  

        btn_layout.setAlignment(Qt.AlignCenter)  
        layout.addLayout(btn_layout)  

        self.setLayout(layout)  

        self.show()  # Показать окно после установки лэйаута  

    def open_file_dialog(self):  
        options = QFileDialog.Options()  
        file_name, _ = QFileDialog.getOpenFileName(self, "Выбор файла", "", options=options)  
        if file_name:  
            self.file_edit.setText(file_name)  
            self.file_path = file_name  

    def open_file_dialog1(self):  
        options = QFileDialog.Options()  
        file_name, _ = QFileDialog.getOpenFileName(self, "Выбор файла", "", options=options)  
        if file_name:  
            self.file_edit1.setText(file_name)  
            self.file_path1 = file_name  

    def close_window(self):  
        self.close()  
        self.main_window.show()  

    def center(self):  
        qr = self.frameGeometry()  
        cp = QDesktopWidget().availableGeometry().center()  
        qr.moveCenter(cp)  
        self.move(qr.topLeft()) 


    def start(self):
        if self.windowTitle() == "сборка генома":
            self.status_label.setWordWrap(True) 
            # Команда для сборки генома
            abyss_command = (
                "abyss-pe k=25 name=test B=1G "
                f"in='{self.file_path1} {self.file_path}'"
            )

            try:
                subprocess.run(abyss_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.status_label.setText(f"Сборка завершена успешно")
            except subprocess.CalledProcessError as e:
                self.status_label.setText(f"Ошибка выполнения команды: {e.stderr.decode('utf-8')}")


        elif self.windowTitle() == "индексация":  
            self.status_label.setWordWrap(True)  

            if self.file_path:  
                if self.file_path.endswith(".fasta") or self.file_path.endswith(".fa") or self.file_path.endswith(".fna"):  
                    try:  
                        subprocess.run(["bwa", "index", self.file_path], check=True)  
                        self.status_label.setText(f"Файл {self.file_path} успешно проиндексирован")
                    except Exception as e:  
                        self.status_label.setText(f"Ошибка при индексировании файла {self.file_path}: {e}")  
                else:
                    self.status_label.setText(f"Выбранный файл {self.file_path} не является файлом в формате FASTA.")  
            else: 
                self.status_label.setText("Пожалуйста, выберите файл FASTA")


        elif self.windowTitle() == "картирование":  
                    self.status_label.setWordWrap(True) 

                    if not self.file_path1 or not self.file_path:  
                        self.status_label.setText("Пожалуйста, сначала выберите файлы, содержащие референсную последовательность, и вашу последовательность.")  
                        return  

                    try:  
                        # Выравнивание прочтений из файла FASTQ на референсный геном и сохранение результата в формате SAM
                        output_sam = os.path.splitext(self.file_path)[0] + ".sam" 
                        subprocess.run(["bwa", "mem", self.file_path1, self.file_path, "-o", output_sam], check=True) 

                        # Преобразование SAM-файла в BAM-файл с помощью samtools
                        output_bam = os.path.splitext(output_sam)[0] + ".bam" 
                        subprocess.run(["samtools", "view", "-Sb", output_sam, "-o", output_bam], check=True) 

                        # Сортировка BAM-файла
                        sorted_bam = os.path.splitext(output_bam)[0] + "_sorted.bam" 
                        subprocess.run(["samtools", "sort", output_bam, "-o", sorted_bam], check=True) 

                        # Индексирование сортированного BAM-файла
                        subprocess.run(["samtools", "index", sorted_bam], check=True) 

                        self.status_label.setText(f"Картирование файла {self.file_path} завершено. Результаты сохранены в {output_sam}. Сортированные и индексированные файл для SNP анализа сохранён в {output_bam}")  
                    except subprocess.CalledProcessError as e:  
                        self.status_label.setText(f"Ошибка при картировании файла {self.file_path}: {e}")  
                    except Exception as e:  
                        self.status_label.setText(f"Ошибка при картировании файла {self.file_path}: {e}")


        elif self.windowTitle() == "SNP и индели":
            self.status_label.setWordWrap(True) 
            self.alignment = self.file_path  # Указываем файл выравнивания
            self.reference = self.file_path1  # Указываем файл референса
            
            if not self.reference or not self.alignment:
                self.status_label.setText("Пожалуйста, сначала выберите файл референса (fasta) и файл выравнивания (bam).")
                return

            try:
                # Временный файл для промежуточных результатов
                mpileup_output = os.path.splitext(self.alignment)[0] + ".mpileup"

                # Команда bcftools mpileup
                mpileup_command = f"bcftools mpileup -f {self.reference} {self.alignment} -o {mpileup_output}"
                subprocess.run(mpileup_command, shell=True, check=True)

                # Команда bcftools call
                call_output = os.path.splitext(self.alignment)[0] + ".bcf"
                call_command = f"bcftools call -mv -Ob -o {call_output} {mpileup_output}"
                subprocess.run(call_command, shell=True, check=True)

                self.status_label.setText(f"Вариантный анализ завершен. Результаты сохранены в {call_output}.")
            except subprocess.CalledProcessError as e:
                self.status_label.setText(f"Ошибка выполнения команды: {e.stderr.decode('utf-8')}")
            except Exception as e:
                self.status_label.setText(f"Неизвестная ошибка: {str(e)}")


        else:
            self.status_label.setWordWrap(True) 
            # Команда для сборки генома с использованием SPAdes 
            spades_command = ( 
                f"spades.py -1 {self.file_path1} -2 {self.file_path} -o spades_output" 
                )

            try:
                subprocess.run(spades_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.status_label.setText(f"Сборка завершена успешно")
            except subprocess.CalledProcessError as e:
                self.status_label.setText(f"Ошибка выполнения команды: {e.stderr.decode('utf-8')}")   

            # Команда для аннотации с использованием prokka 
            prokka_command = f"prokka spades_output/contigs.fasta"

            try:
                subprocess.run(prokka_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.status_label.setText(f"Аннотация завершена успешно! Найдите папку с именем PROKKA_yyyymmdd (сегодняшняя дата) и посмотрите статистику")
            except subprocess.CalledProcessError as e:
                self.status_label.setText(f"Ошибка выполнения команды: {e.stderr.decode('utf-8')}")


class Example(QWidget):  
    def __init__(self):  
        super().__init__()  
        self.init_ui()  

    def init_ui(self):  
        self.resize(850, 550)  
        self.center()  
        self.setStyleSheet("background-color: #66CDAA;")  
        self.setWindowTitle("окошко")  

        layout = QVBoxLayout()  

        btn1 = QPushButton("сборка генома", self)  
        btn2 = QPushButton("индексация", self)  
        btn3 = QPushButton("картирование", self)  
        btn4 = QPushButton("SNP и индели", self)
        btn5 = QPushButton("сборка и аннотация (конвейер)", self)
        btn6 = QPushButton("источники", self)

        for btn in (btn1, btn2, btn3, btn4, btn5):  
            btn.setFixedSize(600, 100)  
            btn.setStyleSheet("background-color: #4CAF50; color: white;")  

        btn1.clicked.connect(lambda: self.open_new_window("сборка генома"))  
        btn2.clicked.connect(lambda: self.open_new_window("индексация"))  
        btn3.clicked.connect(lambda: self.open_new_window("картирование"))  
        btn4.clicked.connect(lambda: self.open_new_window("SNP и индели"))
        btn5.clicked.connect(lambda: self.open_new_window("сборка и аннотация (конвейер)"))  
        btn6.clicked.connect(lambda: self.open_ist("источники"))  


        btn_layout = QVBoxLayout()  
        btn_layout.addWidget(btn1)  
        btn_layout.addWidget(btn2)  
        btn_layout.addWidget(btn3)  
        btn_layout.addWidget(btn4)
        btn_layout.addWidget(btn5)  
        btn_layout.setAlignment(Qt.AlignCenter)  

        layout.addLayout(btn_layout)  
        self.setLayout(layout)  

        self.show()  # Показать главное окно  

    def center(self):  
        qr = self.frameGeometry()  
        cp = QDesktopWidget().availableGeometry().center()  
        qr.moveCenter(cp)  
        self.move(qr.topLeft())  

    def open_new_window(self, title):  
        self.hide()  # Скрываем главное окно  
        self.new_window = NewWindow(title, self)  # Создаем новое окно
    
    def open_ist(self, title):  
        self.hide()  # Скрываем главное окно  
        self.new_window = Ist(title, self)  # Создаем новое окно


class Ist(QWidget):
    def __init__(self, title, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle(title)
        self.init_ui()

    def init_ui(self):
        self.resize(850, 550)
        self.center()
        self.setStyleSheet("background-color: #66CDAA;")
        
        layout = QVBoxLayout()
        self.status_label = QLabel()

        self.status_label = QLabel(self)
        self.status_label.setWordWrap(True)   
        self.status_label.setFixedSize(600, 300)  
        self.status_label.setText(
            "<b>Библиотеки Python:</b><br>"
            "&#8226; <a href='https://github.com/PyQt5'>PyQt5</a><br><br>"
            "<b>Встроенные модули Python:</b><br>"
            "&#8226; <a href='https://github.com/Apubra/python-basic/blob/master/Sys%20Module.py'>sys</a><br>"
            "&#8226; <a href='https://gist.github.com/sseongha11/aab2d1c372372968aee27ce1ca6bc394'>os</a><br>"
            "&#8226; <a href='https://github.com/python/cpython/blob/main/Lib/subprocess.py'>subprocess</a><br><br>"
            "<b>Внешние программы и утилиты:</b><br>"
            "&#8226; <a href='https://github.com/bcgsc/abyss'>ABySS</a><br>"
            "&#8226; <a href='https://github.com/mathworks/bowtie2'>Bowtie2</a><br>"
            "&#8226; <a href='https://github.com/ablab/spades'>SPAdes</a><br>"
            "&#8226; <a href='https://github.com/tseemann/prokka'>Prokka</a><br>"
            "&#8226; <a href='https://github.com/samtools/bcftools'>bcftools</a>"
        )
        self.status_label.setOpenExternalLinks(True) # Открытие ссылок в браузере
        layout.addWidget(self.status_label, alignment=Qt.AlignCenter)



        back_button = QPushButton("Назад", self)
        back_button.clicked.connect(self.close_window)
        back_button.setFixedSize(600, 100)
        back_button.setStyleSheet("background-color: #4CAF50; color: white;")

        # Создание вертикального лэйаута для центрирования кнопок
        btn_layout = QVBoxLayout()
        btn_layout.addWidget(back_button)

        btn_layout.setAlignment(Qt.AlignCenter)
        layout.addLayout(btn_layout)

        self.setLayout(layout)
        self.show()  # Показать окно после установки лэйаута

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def close_window(self):
        self.close()
        self.main_window.show()


if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    ex = Example()  
    sys.exit(app.exec_())

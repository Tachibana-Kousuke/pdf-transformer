import os
import fitz
import markdownify
from pdf2docx import Converter
import customtkinter as ctk
from tkinter import filedialog, messagebox

pdf_files = []

def merge_pdfs():
    if not pdf_files:
        messagebox.showwarning("警告", "请先添加 PDF 文件！")
        return
    
    save_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF 文件", "*.pdf")],
        initialdir="E:/下载/Documents",
        title="选择保存位置"
    )
    
    if not save_path:
        return
    
    try:
        merged_pdf = fitz.open()
        for pdf in pdf_files:
            doc = fitz.open(pdf)
            merged_pdf.insert_pdf(doc)
        merged_pdf.save(save_path)
        merged_pdf.close()
        messagebox.showinfo("成功", f"PDF 已保存到 {save_path}")
    except Exception as e:
        messagebox.showerror("错误", f"合并 PDF 失败: {e}")

def add_pdfs():
    files = filedialog.askopenfilenames(
        filetypes=[("PDF 文件", "*.pdf")],
        title="选择 PDF 文件"
    )
    
    for file in files:
        if file not in pdf_files:
            pdf_files.append(file)
            file_listbox.insert("end", file + "\n")

def clear_list():
    pdf_files.clear()
    file_listbox.delete("1.0", "end")

def pdf_to_txt():
    if not pdf_files:
        messagebox.showwarning("警告", "请先添加 PDF 文件！")
        return

    for pdf in pdf_files:
        try:
            doc = fitz.open(pdf)
            text = ""
            for page_num in range(doc.page_count):
                page = doc.load_page(page_num)
                text += page.get_text("text")

            text = text.replace(r"$$", r"\[\]").replace(r"$", r"\$")

            save_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text 文件", "*.txt")],
                initialdir="E:/下载/Documents",
                title=f"选择保存位置 - {os.path.basename(pdf)}"
            )
            if save_path:
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(text)
                messagebox.showinfo("成功", f"{os.path.basename(pdf)} 已保存为文本文件。")
        except Exception as e:
            messagebox.showerror("错误", f"转换失败: {e}")

def pdf_to_markdown():
    if not pdf_files:
        messagebox.showwarning("警告", "请先添加 PDF 文件！")
        return

    for pdf in pdf_files:
        try:
            doc = fitz.open(pdf)
            text = ""
            for page_num in range(doc.page_count):
                page = doc.load_page(page_num)
                text += page.get_text("text")
            
            markdown_text = markdownify.markdownify(text)
            
            save_path = filedialog.asksaveasfilename(
                defaultextension=".md",
                filetypes=[("Markdown 文件", "*.md")],
                initialdir="E:/下载/Documents",
                title=f"选择保存位置 - {os.path.basename(pdf)}"
            )
            if save_path:
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(markdown_text)
                messagebox.showinfo("成功", f"{os.path.basename(pdf)} 已保存为 Markdown 文件。")
        except Exception as e:
            messagebox.showerror("错误", f"转换失败: {e}")

def pdf_to_word():
    if not pdf_files:
        messagebox.showwarning("警告", "请先添加 PDF 文件！")
        return

    for pdf in pdf_files:
        try:
            save_path = filedialog.asksaveasfilename(
                defaultextension=".docx",
                filetypes=[("Word 文件", "*.docx")],
                initialdir="E:/下载/Documents",
                title=f"选择保存位置 - {os.path.basename(pdf)}"
            )
            if save_path:
                cv = Converter(pdf)
                cv.convert(save_path, start=0, end=None)
                cv.close()
                messagebox.showinfo("成功", f"{os.path.basename(pdf)} 已保存为 Word 文件。")
        except Exception as e:
            messagebox.showerror("错误", f"转换失败: {e}")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("PDF 转换工具")
root.geometry("500x500")

frame = ctk.CTkFrame(root)
frame.pack(pady=10, fill="both", expand=True)

file_listbox = ctk.CTkTextbox(frame, width=450, height=200)
file_listbox.pack(padx=10, pady=10)

btn_add = ctk.CTkButton(root, text="添加 PDF", command=add_pdfs)
btn_add.pack(pady=5)

btn_merge = ctk.CTkButton(root, text="合并 PDF", command=merge_pdfs)
btn_merge.pack(pady=5)

btn_txt = ctk.CTkButton(root, text="PDF 转 TXT", command=pdf_to_txt)
btn_txt.pack(pady=5)

btn_markdown = ctk.CTkButton(root, text="PDF 转 Markdown", command=pdf_to_markdown)
btn_markdown.pack(pady=5)

btn_word = ctk.CTkButton(root, text="PDF 转 Word", command=pdf_to_word)
btn_word.pack(pady=5)

btn_clear = ctk.CTkButton(root, text="清空列表", command=clear_list)
btn_clear.pack(pady=5)

root.mainloop()

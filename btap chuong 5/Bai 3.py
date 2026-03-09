from xml.dom import minidom

def read_xml(filename):
    try:

        doc = minidom.parse(filename)

        employees = doc.getElementsByTagName("employee")

        print("Danh sách nhân viên:\n")

        for emp in employees:

            id_tag = emp.getElementsByTagName("id")[0]
            emp_id = id_tag.firstChild.data.strip()

            name_tag = emp.getElementsByTagName("name")[0]
            emp_name = name_tag.firstChild.data.strip()

            print(f"ID: {emp_id} - Tên: {emp_name}")

    except FileNotFoundError:
        print("Không tìm thấy file XML!")
    except Exception as e:
        print("Lỗi khi đọc XML:", e)

read_xml("employees.xml")
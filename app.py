# import pandas as pd
import streamlit as st

# Cấu hình trang Streamlit
st.set_page_config(
    page_title="Quản Lý Thông Tin Khách Hàng", page_icon="👤", layout="wide"
)

st.title("📋 Quản Lý Thông Tin Khách Hàng")

# Khởi tạo dữ liệu lưu trữ trong session_state
if "customer_list" not in st.session_state:
  st.session_state.customer_list = []

# Chia giao diện thành 2 cột: Cột trái nhập liệu, Cột phải hiển thị danh sách
col1, col2 = st.columns([1, 2])

# --- CỘT 1: FORM NHẬP THÔNG TIN ---
with col1:
  st.subheader("➕ Thêm khách hàng mới")

  with st.form(key="customer_form", clear_on_submit=True):
    phone = st.text_input("Số điện thoại *", placeholder="Ví dụ: 0901234567")
    name = st.text_input("Tên KH *", placeholder="Ví dụ: Nguyễn Văn A")
    region = st.selectbox(
        "Khu vực",
        [
            "Hà Nội",
            "TP. Hồ Chí Minh",
            "Đà Nẵng",
            "Miền Bắc",
            "Miền Trung",
            "Miền Nam",
            "Khác",
        ],
    )
    notes = st.text_area("Ghi chú", placeholder="Nhập thông tin ghi chú...")

    submit_button = st.form_submit_button(
        label="💾 Lưu thông tin", use_container_width=True
    )

    if submit_button:
      # Kiểm tra trường bắt buộc
      if not phone.strip() or not name.strip():
        st.error("Vui lòng điền đầy đủ **Số điện thoại** và **Tên KH**!")
      else:
        # Thêm thông tin vào danh sách
        new_customer = {
            "Số điện thoại": phone.strip(),
            "Tên KH": name.strip(),
            "Khu vực": region,
            "Ghi chú": notes.strip(),
        }
        st.session_state.customer_list.append(new_customer)
        st.success(f"Đã lưu thành công khách hàng: **{name}**")

# --- CỘT 2: HIỂN THỊ VÀ XUẤT DỮ LIỆU ---
with col2:
  st.subheader("📊 Danh sách khách hàng đã nhập")

  if st.session_state.customer_list:
    # Chuyển đổi danh sách thành DataFrame
    df = pd.DataFrame(st.session_state.customer_list)

    # Hiển thị bảng dữ liệu
    st.dataframe(df, use_container_width=True)

    col_down, col_clear = st.columns([1, 1])

    # Nút xuất file CSV (hỗ trợ tiếng Việt UTF-8 BOM)
    with col_down:
      csv_data = df.to_csv(index=False, encoding="utf-8-sig").encode(
          "utf-8-sig"
      )
      st.download_button(
          label="📥 Tải danh sách (File CSV)",
          data=csv_data,
          file_name="danh_sach_khach_hang.csv",
          mime="text/csv",
          use_container_width=True,
      )

    # Nút xóa toàn bộ dữ liệu hiện tại
    with col_clear:
      if st.button("🗑️ Xóa toàn bộ dữ liệu", use_container_width=True):
        st.session_state.customer_list = []
        st.rerun()
  else:
    st.info("Chưa có thông tin khách hàng nào trong hệ thống.")
marketingDVTC

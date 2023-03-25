import scipy.stats as st

mean = 174
std = 8

# а). больше 182 см
p_a = 1 - st.norm.cdf((182 - mean) / std)
print("Вероятность того, что рост больше 182 см: {:.4f}".format(p_a))

# б). больше 190 см
p_b = 1 - st.norm.cdf((190 - mean) / std)
print("Вероятность того, что рост больше 190 см: {:.4f}".format(p_b))

# в). от 166 см до 190 см
p_c = st.norm.cdf((190 - mean) / std) - st.norm.cdf((166 - mean) / std)
print("Вероятность того, что рост от 166 см до 190 см: {:.4f}".format(p_c))

# г). от 166 см до 182 см
p_d = st.norm.cdf((182 - mean) / std) - st.norm.cdf((166 - mean) / std)
print("Вероятность того, что рост от 166 см до 182 см: {:.4f}".format(p_d))

# д). от 158 см до 190 см
p_e = st.norm.cdf((190 - mean) / std) - st.norm.cdf((158 - mean) / std)
print("Вероятность того, что рост от 158 см до 190 см: {:.4f}".format(p_e))

# е). не выше 150 см или не ниже 190 см
p_f = st.norm.cdf((150 - mean) / std) + (1 - st.norm.cdf((190 - mean) / std))
print("Вероятность того, что рост не выше 150 см или не ниже 190 см: {:.4f}".format(p_f))

# ё). не выше 150 см или не ниже 198 см
p_g = st.norm.cdf((150 - mean) / std) + (1 - st.norm.cdf((198 - mean) / std))
print("Вероятность того, что рост не выше 150 см или не ниже 198 см: {:.4f}".format(p_g))

# ж). ниже 166 см
p_h = st.norm.cdf((166 - mean) / std)
print("Вероятность того, что рост ниже 166 см: {:.4f}".format(p_h))

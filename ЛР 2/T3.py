def remaining_n(N0, t, t_half):
  return N0 * (0.5 ** (t / t_half))

def curry_remaining_n(t_half):
  def inner(N0, t):
      return remaining_n(N0, t, t_half)
  return inner

isotopes = {
  'Uranium-238': curry_remaining_n(4.5e9),  # Период полураспада в годах
  'Carbon-14': curry_remaining_n(5730),      # Период полураспада в годах
  'Radon-222': curry_remaining_n(3.8),       # Период полураспада в днях
}

N0 = 1000  # Начальное количество вещества
t = 10000  # Время в годах для расчета

for isotope, func in isotopes.items():
  remaining_amount = func(N0, t)
  print(f"Остаток {isotope} через {t} лет: {remaining_amount:.2f}")

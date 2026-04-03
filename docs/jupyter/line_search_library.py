import numpy as np


def strong_wolfe(
    func,
    grad_func,
    x,
    pk,
    c1=1e-3,
    c2=0.9,
    alpha=1.0,
    alpha_max=100.0,
    max_iters=100,
    verbose=False,
):
    """
    Strong Wolfe condition line search method

    Input:
    func:      the function pointer
    grad_func: the gradien function pointer
    x:         the design variables
    p:         the search direction
    alpha:     the initial estimate for the step length
    alpha_max: the maximum value of alpha

    returns:
    alpha:     the step length satisfying the strong Wolfe conditions
    """

    # Compute the function and the gradient at alpha = 0
    fk = func(x)
    gk = grad_func(x)

    # Compute the dot product of the gradient with the search
    # direction to evaluate the derivative of the merit function
    proj_gk = np.dot(gk, pk)

    # Store the old value of the objective
    fj_old = fk
    proj_gj_old = proj_gk
    alpha_old = 0.0

    for j in range(max_iters):
        # Evaluate the merit function
        fj = func(x + alpha * pk)

        # Evaluate the gradient at the new point
        gj = grad_func(x + alpha * pk)
        proj_gj = np.dot(gj, pk)

        # Check if either the sufficient decrease condition is
        # violated or the objective increased
        if fj > fk + c1 * alpha * proj_gk or (j > 0 and fj > fj_old):
            if verbose:
                print("Sufficient decrease conditions violated: interval found")
            # Zoom and return
            return zoom(
                func,
                grad_func,
                fj_old,
                proj_gj_old,
                alpha_old,
                fj,
                proj_gj,
                alpha,
                x,
                fk,
                gk,
                pk,
                c1=c1,
                c2=c2,
                verbose=verbose,
            )

        # Check if the strong Wolfe conditions are satisfied
        if np.fabs(proj_gj) <= c2 * np.fabs(proj_gk):
            if verbose:
                print("Strong Wolfe alpha found directly")
            func(x + alpha * pk)
            return alpha

        # If the line search is vioalted
        if proj_gj >= 0.0:
            if verbose:
                print("Slope condition violated; interval found")
            return zoom(
                func,
                grad_func,
                fj,
                proj_gj,
                alpha,
                fj_old,
                proj_gj_old,
                alpha_old,
                x,
                fk,
                gk,
                pk,
                c1=c1,
                c2=c2,
                verbose=verbose,
            )

        # Record the old values of alpha and fj
        fj_old = fj
        proj_gj_old = proj_gj
        alpha_old = alpha

        # Pick a new value for alpha
        alpha = min(2.0 * alpha, alpha_max)

        if alpha >= alpha_max:
            print("Line search failed here alpha >= alpha_max")
            return None

    if verbose:
        print("Line search unsuccessful")
    return alpha


def zoom(
    func,
    grad_func,
    f_low,
    proj_low,
    alpha_low,
    f_high,
    proj_high,
    alpha_high,
    x,
    fk,
    gk,
    pk,
    c1=1e-3,
    c2=0.9,
    max_iters=100,
    verbose=False,
):
    """
    Zoom function: Locate a value between alpha_low and alpha_high
    that satisfies the strong Wolfe conditions. Remember:
    alpha_low/alpha_high are step lengths yielding the
    lowest/higher values of the merit function.

    input:
    f_low:      the value of f(x) at alpha_low
    proj_low:   the value of the derivative of phi at alpha_low
    alpha_low:  the value of the step at alpha_low
    f_high:     the value of f(x) at alpha_high
    proj_high:  the value of the derivative of phi at alpha_high
    alpha_high: the value of the step at alpha_high
    x:          the value of the design variables at alpha = 0
    fk:         the value of the function at alpha = 0
    gk:         the gradient of the function at alpha = 0
    pk:         the line search direction

    returns:
    alpha:   a step length satisfying the strong Wolfe conditions
    """

    proj_gk = np.dot(pk, gk)

    for j in range(max_iters):
        # Pick an alpha value using cubic interpolation
        # alpha_j = cubic_interp(alpha_low, f_low, proj_low,
        #                        alpha_high, f_high, proj_high)

        # Pick an alpha value by bisecting the interval
        alpha_j = 0.5 * (alpha_high + alpha_low)

        # Evaluate the merit function
        fj = func(x + alpha_j * pk)

        # Check if the sufficient decrease condition is violated
        if fj > fk + c1 * alpha_j * proj_gk or fj >= f_low:
            if verbose:
                print("Zoom: Sufficient decrease conditions violated")
            alpha_high = alpha_j
            f_high = fj

            # We need the derivative here for proj_high
            gj = grad_func(x + alpha_j * pk)
            proj_high = np.dot(gj, pk)
        else:
            # Evaluate the gradient of the function and the
            # derivative of the merit function
            gj = grad_func(x + alpha_j * pk)
            proj_gj = np.dot(gj, pk)

            # Return alpha, the strong Wolfe conditions are
            # satisfied
            if np.fabs(proj_gj) <= c2 * np.fabs(proj_gk):
                if verbose:
                    print("Zoom: Wolfe conditions satisfied")
                func(x + alpha_j * pk)
                return alpha_j
            elif verbose:
                print("Zoom: Curvature condition violated")

            # Make sure that we have the intervals right
            if proj_gj * (alpha_high - alpha_low) >= 0.0:
                # Swap alpha high/alpha low
                alpha_high = alpha_low
                proj_high = proj_low
                f_high = f_low

            # Swap alpha low/alpha j
            alpha_low = alpha_j
            proj_low = proj_gj
            f_low = fj

    return alpha_j


def cubic_interp(self, x0, m0, dm0, x1, m1, dm1, verbose=False):
    """
    Return an x in the interval (x0, x1) that minimizes a cubic
    interpolant between two points with both function and
    derivative values.

    This method does not assume that x0 > x1. If the solution is
    not in the interval, the function returns the mid-point.
    """

    # Compute d1
    d1 = dm0 + dm1 - 3 * (m0 - m1) / (x0 - x1)

    # Check that the square root will be real in the
    # expression for d2
    if (d1**2 - dm0 * dm1) < 0.0:
        if verbose:
            print("Cubic interpolation fail")
        return 0.5 * (x0 + x1)

    # Compute d2
    d2 = np.sign(x1 - x0) * np.sqrt(d1**2 - dm0 * dm1)

    # Evaluate the new interpolation point
    x = x1 - (x1 - x0) * (dm1 + d2 - d1) / (dm1 - dm0 + 2 * d2)

    # If the new point is outside the interval, return
    # the mid point
    if x1 > x0 and (x > x1 or x < x0):
        return 0.5 * (x0 + x1)
    elif x0 > x1 and (x > x0 or x < x1):
        return 0.5 * (x0 + x1)

    return x

title: Why was "scipy.misc" removed, and what's next?
slug: why-was-scipy-misc-removed-and-whats-next
pub: 2022-10-18 06:44:17
authors: abdulkhan
tags: scipy, ecosystem, updates
category: data science
related_posts: whats-new-in-python-3-9-alpha2,python-engineering-articles,free-python-courses-list

Miscellaneous routines in scipy included convenient functions. This article cover the removal of this feature.

Table of content
================


* Why was `_Miscellaneous routines_` removed from `SciPy`?
* A Very Brief Introduction to `scipy.datasets`
    + What does this implement/fix ?
* Pooch and scipy.datasets partnership


Why was `_Miscellaneous routines_` removed from `SciPy`?
========================================================



Back in the olden days *the Miscellaneous routines* of Scipy used to have some importance. But in 2022 it only has five methods `ascent()`, `central_diff_weights`, `derivative`, `face`, `electrocardiogram`. Most of these methods have moved under some other module/submodule and many Users have complaints about the usefulness/computational inefficiencies of this submodule. For example:


> 
>  " [Stephan Hoyer](https://mail.python.org/archives/users/fd539a97c2b34c4f82f9729ad7f4eb17/)
>  I would vote for removing them entirely, I haven't used either of
>  them, it just came up in a search for finite differences in Python"
> 


**Because `scipy.misc` is a submodule** with five methods only. This increases the package size of the Library and comprises optimization, *an overall decrease in the processing speed of other methods.*
Considering all the reasons given above people were now Frustrated with this! ↓


> 
>  in 2018 An enthusiast [Warren
>  Weckesser](https://github.com/scipy/scipy/pull/8707) created a pull
>  request to remove `.misc` from SciPy **And introduce a new Idea
>  `scipy.datasets`** for some unfortunate reasons it did not proceed.
>  ↓ 
>  This year [Anirudh Dagar](https://mail.python.org/archives/list/scipy-dev@python.org/thread/AACMUJES2D3F24QWSQNOBVIYBOUZD2QX/)
>  Picked up this idea and eventually convinced the Scipy Maintainers to add `scipy.datasets` as a submodule (which includes all methods of `.misc`)
> 


A Very Brief Introduction to `scipy.datasets`
=============================================



```python
>>> from scipy import datasets
# Example ascent dataset loading with the new module
>>> datasets.ascent()
array([[ 83, 83, 83, ..., 117, 117, 117],
 [ 82, 82, 83, ..., 117, 117, 117],
 [ 80, 81, 83, ..., 117, 117, 117],
 ...,
 [178, 178, 178, ..., 57, 59, 57],
 [178, 178, 178, ..., 56, 57, 57],
 [178, 178, 178, ..., 57, 57, 58]])

```

What does this implement/fix ?
------------------------------


With [gh-8707](https://github.com/scipy/scipy/pull/8707), in 2018, SciPy wanted to introduce the `datasets` submodule and move a handful of dataset functions from the current `misc` module to this new `datasets` submodule. **A Big Thanks to [@WarrenWeckesser](https://github.com/WarrenWeckesser) for discovering this idea.** With this PR (indeed inspired by [gh-8707](https://github.com/scipy/scipy/pull/8707)) they ([Anirudh](https://mail.python.org/archives/users/d23be19d7818404998f29c9c1ea3d1f9/) and [Ralf](https://mail.python.org/archives/users/f60feb983fc549cba6161c320da7b574/)) resume those efforts after making some improvements (explained below) and move away from the `scipy.misc` module, finally deprecating it in a separate PR [#15901](https://github.com/scipy/scipy/pull/15901))

* Add `scipy.datasets` submodule
* Utilize [pooch](https://github.com/fatiando/pooch) to handle the dataset downloading and caching.
* Enable meson support for `scipy.datasets` submodule
* Move all dataset files (eg. `scipy.stats` has its own [test datasets](https://github.com/scipy/scipy/tree/main/scipy/stats/tests/data) within the repository) to their respective new repository (explained below). This is something that can be done after landing this PR once we have a concrete datasets API and approach defined for adding new datasets.
* Deprecate the misc module ([DEP: Deprecate scipy.misc in favour of scipy.datasets #15901](https://github.com/scipy/scipy/pull/15901))


Pooch and scipy.datasets partnership
====================================



Pooch manages data registrations by downloading your data files from a server only when needed and storing them locally in a data *cache* (a folder on your computer).

* With `Pooch` you can easily decouple the datasets that are currently present within the `SicPy` repository and move them to their new repository. For example, see <https://github.com/scipy-datasets>, where each dataset has its own repository. This will lead to a lightweight `SciPy` Package decreasing the download size for future releases. Keeping the datasets in individual repositories or a single `scipy-datasets` repository is a point of discussion.....
* Dependency: Pooch is an extremely light package and has only a few [dependencies](https://github.com/fatiando/pooch/blob/main/setup.cfg#L43-L46), so if you were to add a new dependency i.e. Pooch, you can expect it to be small and at the same time it won't add a lot of sub-dependencies.




References
==========


* [scipy-dev](https://mail.python.org/archives/list/scipy-dev@python.org/thread/AACMUJES2D3F24QWSQNOBVIYBOUZD2QX/)


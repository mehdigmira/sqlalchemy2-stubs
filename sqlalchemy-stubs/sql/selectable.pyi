from typing import Any
from typing import Optional

from . import coercions as coercions
from . import operators as operators
from . import roles as roles
from . import type_api as type_api
from .annotation import Annotated as Annotated
from .annotation import SupportsCloneAnnotations as SupportsCloneAnnotations
from .base import CacheableOptions as CacheableOptions
from .base import ColumnCollection as ColumnCollection
from .base import ColumnSet as ColumnSet
from .base import CompileState as CompileState
from .base import DedupeColumnCollection as DedupeColumnCollection
from .base import Executable as Executable
from .base import Generative as Generative
from .base import HasCompileState as HasCompileState
from .base import HasMemoized as HasMemoized
from .base import Immutable as Immutable
from .base import prefix_anon_map as prefix_anon_map
from .elements import and_ as and_
from .elements import BindParameter as BindParameter
from .elements import BooleanClauseList as BooleanClauseList
from .elements import ClauseElement as ClauseElement
from .elements import ClauseList as ClauseList
from .elements import ColumnClause as ColumnClause
from .elements import GroupedElement as GroupedElement
from .elements import Grouping as Grouping
from .elements import literal_column as literal_column
from .elements import TableValuedColumn as TableValuedColumn
from .elements import UnaryExpression as UnaryExpression
from .visitors import InternalTraversal as InternalTraversal
from .. import exc as exc
from .. import util as util

class _OffsetLimitParam(BindParameter):
    inherit_cache: bool = ...

def subquery(alias: Any, *args: Any, **kwargs: Any): ...

class ReturnsRows(roles.ReturnsRowsRole, ClauseElement):
    @property
    def selectable(self) -> None: ...
    @property
    def exported_columns(self) -> None: ...

class Selectable(ReturnsRows):
    __visit_name__: str = ...
    is_selectable: bool = ...
    @property
    def selectable(self): ...
    def lateral(self, name: Optional[Any] = ...): ...
    def replace_selectable(self, old: Any, alias: Any): ...
    def corresponding_column(
        self, column: Any, require_embedded: bool = ...
    ): ...

class HasPrefixes:
    def prefix_with(self, *expr: Any, **kw: Any) -> None: ...

class HasSuffixes:
    def suffix_with(self, *expr: Any, **kw: Any) -> None: ...

class HasHints:
    def with_statement_hint(self, text: Any, dialect_name: str = ...): ...
    def with_hint(
        self, selectable: Any, text: Any, dialect_name: str = ...
    ) -> None: ...

class FromClause(roles.AnonymizedFromClauseRole, Selectable):
    __visit_name__: str = ...
    named_with_column: bool = ...
    schema: Any = ...
    is_selectable: bool = ...
    def select(self, whereclause: Optional[Any] = ..., **kwargs: Any): ...
    def join(
        self,
        right: Any,
        onclause: Optional[Any] = ...,
        isouter: bool = ...,
        full: bool = ...,
    ): ...
    def outerjoin(
        self, right: Any, onclause: Optional[Any] = ..., full: bool = ...
    ): ...
    def alias(self, name: Optional[Any] = ..., flat: bool = ...): ...
    def table_valued(self): ...
    def tablesample(
        self,
        sampling: Any,
        name: Optional[Any] = ...,
        seed: Optional[Any] = ...,
    ): ...
    def is_derived_from(self, fromclause: Any): ...
    @property
    def description(self): ...
    @property
    def exported_columns(self): ...
    def columns(self): ...
    @property
    def entity_namespace(self): ...
    def primary_key(self): ...
    def foreign_keys(self): ...
    c: Any = ...

LABEL_STYLE_NONE: Any
LABEL_STYLE_TABLENAME_PLUS_COL: Any
LABEL_STYLE_DISAMBIGUATE_ONLY: Any
LABEL_STYLE_DEFAULT = LABEL_STYLE_DISAMBIGUATE_ONLY

class Join(roles.DMLTableRole, FromClause):
    __visit_name__: str = ...
    left: Any = ...
    right: Any = ...
    onclause: Any = ...
    isouter: Any = ...
    full: Any = ...
    def __init__(
        self,
        left: Any,
        right: Any,
        onclause: Optional[Any] = ...,
        isouter: bool = ...,
        full: bool = ...,
    ) -> None: ...
    @property
    def description(self): ...
    def is_derived_from(self, fromclause: Any): ...
    def self_group(self, against: Optional[Any] = ...): ...
    def select(self, whereclause: Optional[Any] = ..., **kwargs: Any): ...
    @property
    def bind(self): ...
    def alias(self, name: Optional[Any] = ..., flat: bool = ...): ...

class NoInit:
    def __init__(self, *arg: Any, **kw: Any) -> None: ...

class AliasedReturnsRows(NoInit, FromClause):
    named_with_column: bool = ...
    @property
    def description(self): ...
    @property
    def original(self): ...
    def is_derived_from(self, fromclause: Any): ...
    @property
    def bind(self): ...

class Alias(roles.DMLTableRole, AliasedReturnsRows):
    __visit_name__: str = ...
    inherit_cache: bool = ...

class TableValuedAlias(Alias):
    __visit_name__: str = ...
    def column(self): ...
    def alias(self, name: Optional[Any] = ...): ...
    def lateral(self, name: Optional[Any] = ...): ...
    def render_derived(
        self, name: Optional[Any] = ..., with_types: bool = ...
    ): ...

class Lateral(AliasedReturnsRows):
    __visit_name__: str = ...
    inherit_cache: bool = ...

class TableSample(AliasedReturnsRows):
    __visit_name__: str = ...

class CTE(Generative, HasPrefixes, HasSuffixes, AliasedReturnsRows):
    __visit_name__: str = ...
    def alias(self, name: Optional[Any] = ..., flat: bool = ...): ...
    def union(self, other: Any): ...
    def union_all(self, other: Any): ...

class HasCTE(roles.HasCTERole):
    def cte(self, name: Optional[Any] = ..., recursive: bool = ...): ...

class Subquery(AliasedReturnsRows):
    __visit_name__: str = ...
    inherit_cache: bool = ...
    def as_scalar(self): ...

class FromGrouping(GroupedElement, FromClause):
    element: Any = ...
    def __init__(self, element: Any) -> None: ...
    @property
    def columns(self): ...
    @property
    def primary_key(self): ...
    @property
    def foreign_keys(self): ...
    def is_derived_from(self, element: Any): ...
    def alias(self, **kw: Any): ...

class TableClause(roles.DMLTableRole, Immutable, FromClause):
    __visit_name__: str = ...
    named_with_column: bool = ...
    implicit_returning: bool = ...
    name: Any = ...
    primary_key: Any = ...
    foreign_keys: Any = ...
    schema: Any = ...
    def __init__(self, name: Any, *columns: Any, **kw: Any) -> None: ...
    def description(self): ...
    def append_column(self, c: Any, **kw: Any) -> None: ...
    def insert(
        self, values: Optional[Any] = ..., inline: bool = ..., **kwargs: Any
    ): ...
    def update(
        self,
        whereclause: Optional[Any] = ...,
        values: Optional[Any] = ...,
        inline: bool = ...,
        **kwargs: Any,
    ): ...
    def delete(self, whereclause: Optional[Any] = ..., **kwargs: Any): ...

class ForUpdateArg(ClauseElement):
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    nowait: Any = ...
    read: Any = ...
    skip_locked: Any = ...
    key_share: Any = ...
    of: Any = ...
    def __init__(
        self,
        nowait: bool = ...,
        read: bool = ...,
        of: Optional[Any] = ...,
        skip_locked: bool = ...,
        key_share: bool = ...,
    ) -> None: ...

class Values(Generative, FromClause):
    named_with_column: bool = ...
    __visit_name__: str = ...
    name: Any = ...
    literal_binds: Any = ...
    def __init__(self, *columns: Any, **kw: Any) -> None: ...
    def alias(self, name: Any, **kw: Any) -> None: ...
    def lateral(self, name: Optional[Any] = ...) -> None: ...
    def data(self, values: Any) -> None: ...

class SelectBase(
    roles.SelectStatementRole,
    roles.DMLSelectRole,
    roles.CompoundElementRole,
    roles.InElementRole,
    HasCTE,
    Executable,
    SupportsCloneAnnotations,
    Selectable,
):
    is_select: bool = ...
    @property
    def selected_columns(self) -> None: ...
    @property
    def exported_columns(self): ...
    @property
    def c(self): ...
    @property
    def columns(self): ...
    def select(self, *arg: Any, **kw: Any): ...
    def as_scalar(self): ...
    def exists(self): ...
    def scalar_subquery(self): ...
    def label(self, name: Any): ...
    def lateral(self, name: Optional[Any] = ...): ...
    def subquery(self, name: Optional[Any] = ...): ...
    def alias(self, name: Optional[Any] = ..., flat: bool = ...): ...

class SelectStatementGrouping(GroupedElement, SelectBase):
    __visit_name__: str = ...
    element: Any = ...
    def __init__(self, element: SelectBase) -> None: ...
    def get_label_style(self): ...
    def set_label_style(self, label_style: Any): ...
    @property
    def select_statement(self): ...
    def self_group(self, against: Optional[Any] = ...) -> FromClause: ...
    @property
    def selected_columns(self): ...

class DeprecatedSelectBaseGenerations:
    def append_order_by(self, *clauses: Any) -> None: ...
    def append_group_by(self, *clauses: Any) -> None: ...

class GenerativeSelect(DeprecatedSelectBaseGenerations, SelectBase):
    def __init__(
        self,
        _label_style: Any = ...,
        use_labels: bool = ...,
        limit: Optional[Any] = ...,
        offset: Optional[Any] = ...,
        order_by: Optional[Any] = ...,
        group_by: Optional[Any] = ...,
        bind: Optional[Any] = ...,
    ) -> None: ...
    def with_for_update(
        self,
        nowait: bool = ...,
        read: bool = ...,
        of: Optional[Any] = ...,
        skip_locked: bool = ...,
        key_share: bool = ...,
    ) -> None: ...
    def get_label_style(self): ...
    def set_label_style(self, style: Any): ...
    def apply_labels(self): ...
    def limit(self, limit: Any) -> None: ...
    def fetch(
        self, count: Any, with_ties: bool = ..., percent: bool = ...
    ) -> None: ...
    def offset(self, offset: Any) -> None: ...
    def slice(self, start: Any, stop: Any) -> None: ...
    def order_by(self, *clauses: Any) -> None: ...
    def group_by(self, *clauses: Any) -> None: ...

class CompoundSelectState(CompileState): ...

class CompoundSelect(HasCompileState, GenerativeSelect):
    __visit_name__: str = ...
    UNION: Any = ...
    UNION_ALL: Any = ...
    EXCEPT: Any = ...
    EXCEPT_ALL: Any = ...
    INTERSECT: Any = ...
    INTERSECT_ALL: Any = ...
    keyword: Any = ...
    selects: Any = ...
    def __init__(self, keyword: Any, *selects: Any, **kwargs: Any) -> None: ...
    def self_group(self, against: Optional[Any] = ...) -> FromClause: ...
    def is_derived_from(self, fromclause: Any): ...
    @property
    def selected_columns(self): ...
    @property
    def bind(self): ...
    @bind.setter
    def bind(self, bind: Any) -> None: ...

class DeprecatedSelectGenerations:
    def append_correlation(self, fromclause: Any) -> None: ...
    def append_column(self, column: Any) -> None: ...
    def append_prefix(self, clause: Any) -> None: ...
    def append_whereclause(self, whereclause: Any) -> None: ...
    def append_having(self, having: Any) -> None: ...
    def append_from(self, fromclause: Any) -> None: ...

class SelectState(util.MemoizedSlots, CompileState):
    class default_select_compile_options(CacheableOptions): ...
    statement: Any = ...
    from_clauses: Any = ...
    froms: Any = ...
    columns_plus_names: Any = ...
    def __init__(self, statement: Any, compiler: Any, **kw: Any) -> None: ...
    @classmethod
    def get_column_descriptions(cls, statement: Any) -> None: ...
    @classmethod
    def from_statement(cls, statement: Any, from_statement: Any) -> None: ...
    @classmethod
    def determine_last_joined_entity(cls, stmt: Any): ...
    @classmethod
    def exported_columns_iterator(cls, statement: Any): ...

class _SelectFromElements: ...

class Select(
    HasPrefixes,
    HasSuffixes,
    HasHints,
    HasCompileState,
    DeprecatedSelectGenerations,
    _SelectFromElements,
    GenerativeSelect,
):
    __visit_name__: str = ...
    @classmethod
    def create_legacy_select(
        cls,
        columns: Optional[Any] = ...,
        whereclause: Optional[Any] = ...,
        from_obj: Optional[Any] = ...,
        distinct: bool = ...,
        having: Optional[Any] = ...,
        correlate: bool = ...,
        prefixes: Optional[Any] = ...,
        suffixes: Optional[Any] = ...,
        **kwargs: Any,
    ): ...
    def __init__(self) -> None: ...
    def filter(self, *criteria: Any): ...
    def filter_by(self, **kwargs: Any): ...
    @property
    def column_descriptions(self): ...
    def from_statement(self, statement: Any): ...
    def join(
        self,
        target: Any,
        onclause: Optional[Any] = ...,
        isouter: bool = ...,
        full: bool = ...,
    ) -> None: ...
    def outerjoin_from(
        self,
        from_: Any,
        target: Any,
        onclause: Optional[Any] = ...,
        full: bool = ...,
    ): ...
    def join_from(
        self,
        from_: Any,
        target: Any,
        onclause: Optional[Any] = ...,
        isouter: bool = ...,
        full: bool = ...,
    ) -> None: ...
    def outerjoin(
        self, target: Any, onclause: Optional[Any] = ..., full: bool = ...
    ): ...
    @property
    def froms(self): ...
    @property
    def inner_columns(self): ...
    def is_derived_from(self, fromclause: Any): ...
    def get_children(self, **kwargs: Any): ...
    def add_columns(self, *columns: Any) -> None: ...
    def column(self, column: Any): ...
    def reduce_columns(self, only_synonyms: bool = ...): ...
    def with_only_columns(self, *columns: Any) -> None: ...
    @property
    def whereclause(self): ...
    def where(self, *whereclause: Any) -> None: ...
    def having(self, having: Any) -> None: ...
    def distinct(self, *expr: Any) -> None: ...
    def select_from(self, *froms: Any) -> None: ...
    def correlate(self, *fromclauses: Any) -> None: ...
    def correlate_except(self, *fromclauses: Any) -> None: ...
    def selected_columns(self): ...
    def self_group(self, against: Optional[Any] = ...): ...
    def union(self, other: Any, **kwargs: Any): ...
    def union_all(self, other: Any, **kwargs: Any): ...
    def except_(self, other: Any, **kwargs: Any): ...
    def except_all(self, other: Any, **kwargs: Any): ...
    def intersect(self, other: Any, **kwargs: Any): ...
    def intersect_all(self, other: Any, **kwargs: Any): ...
    @property
    def bind(self): ...
    @bind.setter
    def bind(self, bind: Any) -> None: ...

class ScalarSelect(roles.InElementRole, Generative, Grouping):
    inherit_cache: bool = ...
    element: Any = ...
    type: Any = ...
    def __init__(self, element: Any) -> None: ...
    @property
    def columns(self) -> None: ...
    c: Any = ...
    def where(self, crit: Any) -> None: ...
    def self_group(self, **kwargs: Any): ...
    def correlate(self, *fromclauses: Any) -> None: ...
    def correlate_except(self, *fromclauses: Any) -> None: ...

class Exists(UnaryExpression):
    inherit_cache: bool = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def select(self, whereclause: Optional[Any] = ..., **kwargs: Any): ...
    def correlate(self, *fromclause: Any): ...
    def correlate_except(self, *fromclause: Any): ...
    def select_from(self, *froms: Any): ...
    def where(self, clause: Any): ...

class TextualSelect(SelectBase):
    __visit_name__: str = ...
    is_text: bool = ...
    is_select: bool = ...
    element: Any = ...
    column_args: Any = ...
    positional: Any = ...
    def __init__(
        self, text: Any, columns: Any, positional: bool = ...
    ) -> None: ...
    def selected_columns(self): ...
    def bindparams(self, *binds: Any, **bind_as_values: Any) -> None: ...

TextAsFrom = TextualSelect

class AnnotatedFromClause(Annotated):
    def __init__(self, element: Any, values: Any) -> None: ...